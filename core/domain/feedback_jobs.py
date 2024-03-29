# coding: utf-8
#
# Copyright 2015 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Jobs for open feedback threads."""

from core import jobs
from core.platform import models
(base_models, feedback_models, exp_models,) = models.Registry.import_models([
    models.NAMES.base_model, models.NAMES.feedback, models.NAMES.exploration
])
transaction_services = models.Registry.import_transaction_services()


class FeedbackAnalyticsRealtimeModel(
        jobs.BaseRealtimeDatastoreClassForContinuousComputations):
    pass


class FeedbackAnalyticsAggregator(jobs.BaseContinuousComputationManager):
    """A continuous-computation job that computes analytics for feedback
    threads of explorations.

    This job does not have a realtime component. There will be a delay in
    propagating new updates to the dashboard; the length of the delay will be
    approximately the time it takes a batch job to run.
    """
    # TODO(sll): Add a realtime component: listen to incoming feedback messages
    # and adjust the counts appropriately.

    @classmethod
    def get_event_types_listened_to(cls):
        return []

    @classmethod
    def _get_realtime_datastore_class(cls):
        return FeedbackAnalyticsRealtimeModel

    @classmethod
    def _get_batch_job_manager_class(cls):
        return FeedbackAnalyticsMRJobManager

    @classmethod
    def _handle_incoming_event(cls, active_realtime_layer, event_type, *args):
        pass

    # Public query methods.
    @classmethod
    def get_thread_analytics(cls, exploration_id):
        """
        Args:
          - exploration_id: id of the exploration to get statistics for.

        Returns a dict with two keys: 'num_open_threads' and
        'num_total_threads', representing the counts of open and all feedback
        threads, respectively.
        """
        feedback_thread_analytics_model = (
            feedback_models.FeedbackAnalyticsModel.get(
                exploration_id, strict=False))

        num_open_threads = 0
        num_total_threads = 0
        if feedback_thread_analytics_model:
            num_open_threads = feedback_thread_analytics_model.num_open_threads
            num_total_threads = (
                feedback_thread_analytics_model.num_total_threads)

        return {
            'num_open_threads': num_open_threads,
            'num_total_threads': num_total_threads
        }


class FeedbackAnalyticsMRJobManager(
        jobs.BaseMapReduceJobManagerForContinuousComputations):
    """Job that creates FeedbackAnalyticsModels for explorations by calculating
    various analytics for feedback threads corresponding to an exploration.

    Currently, this job calculates the number of open feedback threads, as well
    as the total feedback thread count for each exploration.
    """

    @classmethod
    def _get_continuous_computation_class(cls):
        return FeedbackAnalyticsAggregator

    @classmethod
    def entity_classes_to_map_over(cls):
        return [feedback_models.FeedbackThreadModel]

    @staticmethod
    def map(item):
        yield (item.exploration_id, item.status)

    @staticmethod
    def reduce(key, stringified_values):
        num_open_threads = stringified_values.count(
            feedback_models.STATUS_CHOICES_OPEN)
        num_total_threads = len(stringified_values)

        feedback_models.FeedbackAnalyticsModel.create(
            key, num_open_threads, num_total_threads)
