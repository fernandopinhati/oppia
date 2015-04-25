# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from extensions.rich_text_components import base


class Html5Video(base.BaseRichTextComponent):
    """A rich-text component representing an HTML5 video."""

    name = 'HTML5 Video'
    category = 'Basic Input'
    description = 'An HTML5 video (of type mp4) from a URL.'
    frontend_name = 'html5_video'
    tooltip = 'Insert HTML5 video'

    _customization_arg_specs = [{
        'name': 'video_url',
        'description': 'The URL source for this video.',
        'schema': {
            'type': 'unicode',
        },
        'default_value': '',
    }]

    # TODO(sll): Replace this.
    icon_data_url = (
        'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAA'
        'ABGdBTUEAAK/INwWK6QAAABl0RVh0%0AU29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZ'
        'TwAAAIfSURBVDjLpZNPaBNBGMXfbrubzBqbg4kL%0A0lJLgiVKE/AP6Kl6UUFQNAeDIAj'
        'VS08aELx59GQPAREV/4BeiqcqROpRD4pUNCJSS21OgloISWME%0AZ/aPb6ARdNeTCz92m'
        'O%2B9N9/w7RphGOJ/nsH%2Bolqtvg%2BCYJR8q9VquThxuVz%2BoJTKeZ63Uq/XC38E%0'
        'A0Jj3ff8%2BOVupVGLbolkzQw5HOqAxQU4wXWWnZrykmYD0QsgAOJe9hpEUcPr8i0GaJ8'
        'n2vs/sL2h8%0AR66TpVfWTdETHWE6GRGKjGiiKNLii5BSLpN7pBHpgMYhMkm8tPUWz3sL'
        '2D1wFaY/jvnWcTTaE5Dy%0AjMfTT5J0XIAiTRYn3ASwZ1MKbTmN7z%2BKaHUOYqmb1fcP'
        'iNa4kQBuyvWAHYfcHGzDgYcx9NKrwJYH%0ACAyF21JiPWBnXMAQOea6bmn%2B4ueYGZi8'
        'gtymNVobF7BG5prNpjd%2BeW6X4BSUD0gOdCpzA8MpA/v2%0Av15kl4%2BpK0emwHSbjJ'
        'GBlz%2BvYM1fQeDrYOBTdzOGvDf6EFNr%2BLYjHbBgsaCLxr%2BmoNQjU2vYhRXp%0AgI'
        'UOmSWWnsJRfjlOZhrexgtYDZ/gWbetNRbNs6QT10GJglNk64HMaGgbAkoMo5fiFNy7CKD'
        'QUGqE%0A5r38YktxAfSqW7Zt33l66WtkAkACjuNsaLVaDxlw5HdJ/86aYrG4WCgUZD6fX'
        '%2Bjv/U0ymfxoWVZo%0AmuZyf%2B8XqfGP49CCrBUAAAAASUVORK5CYII%3D%0A'
    )
