# G5 TV Launcher themes

[English](README.md) · [Deutsch](README.de.md)

## Static themes

[Spring](fruehling.json) · [Summer](sommer.json) · [Autumn](herbst.json) · [Winter](winter.json)

## Animated themes

[Cyberpunk Neon](cyberpunk-neon.json) · [Beach](strand-vektor.json)

[Theme template](template.json)

The file importer and category selection are included in **0.2.70**. These examples were tested through the user's TV import flow; the exact appearance depends on the TV. This is an experimental format and may change in a future version.

**Compatibility:** Beach requires the scene support in test build 0.2.72. Cyberpunk Neon needs a test build with imported-theme animations. The published 0.2.70 version does not support those animations.

**Animations:** Effects for imported themes and `animationOptions` are only available in the newer test build, not in the published 0.2.70 IPK. The new customization options have not yet been tested on a TV. Import and the neon effect were tried on the user's TV with the test build; other effects have not yet been confirmed on a TV. Older themes without an animation field remain compatible.

## Import on a rooted TV

1. Download a theme JSON file. Transfer it with SFTP, for example using Termius, directly to `/tmp` on the TV. Files in `/tmp` are temporary; keep your own copy.
2. In the launcher open **Settings → Appearance → Custom themes**. Select **Find files**, pick the theme file and choose **Import file**.
3. Under **Theme category**, choose **Imported themes**, then choose the theme under **Background**. Up to three custom themes can be stored; remove one in Custom themes to make room. The source file on `/tmp` is separate from the imported copy.

The file selector accepts suitable theme JSON files directly inside `/tmp`; it ignores unrelated JSON and does not browse subfolders. On versions with the JSON input field, a complete theme JSON can also be pasted and installed there. This is not a URL importer.

## Create a theme

Copy [template.json](template.json), edit it as UTF-8 and save it with an ASCII filename ending in `.json`, for example `my-theme.json`:

| Field | Meaning |
| --- | --- |
| `format` | Must be `g5-theme`. |
| `version` | Number `1`. |
| `id` | Unique ID, 1–32 lowercase ASCII letters, digits or hyphens. Reusing an ID replaces that imported theme. |
| `name` | Display name, 1–60 characters. |
| `background` | Background color as `#RRGGBB`. |
| `accent` | Accent color as `#RRGGBB`. |
| `glow` | Glow color as `#RRGGBB`. |
| `animation` | Optional: `none`, `neon`, `rain`, `snow` or `particles`; defaults to `none`. These are built-in launcher effects. Enable animations in the launcher settings. Effects appear in the background banner. |
| `animationOptions` | Optional object for configuring the chosen effect; see the fields below. Available only in the supporting test build. |
| `scene` | Optional shapes and individual animations; see below. Requires test build 0.2.72. |
| `image` | Optional background image as a `data:image/png;base64,...`, `data:image/jpeg;base64,...` or `data:image/webp;base64,...` data URL, at most 70,000 characters including the prefix. Omit it for a solid-color background. |

The complete file must be at most 80,000 bytes. Theme files contain data, not code: scripts, external URLs and SVG image data are not accepted. The format changes colors and the background image; the supporting test build can also apply a selectable built-in animation effect. Custom animation scripts and changes to the overall launcher layout are not supported. Use original artwork or artwork you have permission to share; include attribution and license information when distributing it.

### Customize an animation

The optional `animationOptions` object accepts the fields below. Omitted fields retain the effect's defaults. Use a decimal point in JSON.

| Field | Allowed value | Effect |
| --- | --- | --- |
| `color` | Color as `#RRGGBB` | Effect color. |
| `duration` | Number from 0.5 to 30 | Duration of one cycle in seconds; smaller values are faster. |
| `opacity` | Number from 0 to 1 | Effect opacity; 0 is invisible. |
| `direction` | `normal`, `reverse` or `alternate` | Animation playback direction. |

These parameters adjust a predefined banner effect; they do not create freely programmable animations. Enable animations in the launcher settings. Customize the example or the [template](template.json):

```json
{
  "format": "g5-theme",
  "version": 1,
  "id": "my-first-theme",
  "name": "My first theme",
  "background": "#102030",
  "accent": "#80d0ff",
  "glow": "#4466aa",
  "animation": "neon",
  "animationOptions": {
    "color": "#ff45d4",
    "duration": 4,
    "opacity": 0.75,
    "direction": "alternate"
  },
  "scene": [
    {
      "type": "rect",
      "x": 100,
      "y": 250,
      "width": 180,
      "height": 80,
      "color": "#5bbfd1",
      "animation": {
        "type": "move",
        "duration": 4,
        "dx": 30,
        "dy": 0
      }
    },
    {
      "type": "ellipse",
      "x": 720,
      "y": 45,
      "width": 90,
      "height": 90,
      "color": "#ffd778",
      "animation": {
        "type": "blink",
        "duration": 4
      }
    },
    {
      "type": "polygon",
      "points": [
        [
          600,
          400
        ],
        [
          650,
          300
        ],
        [
          700,
          400
        ]
      ],
      "color": "#4fa977",
      "animation": {
        "type": "sway",
        "duration": 5
      }
    }
  ]
}
```

## Custom scenes with individual animations

**Test status:** The `scene` field requires test build **0.2.72**. Published launcher 0.2.70 and the older 0.2.71 test build do not draw these scene elements. The user tested scene import and basic rendering on a TV; not every combination has been tested.

`scene` is a list of up to 100 shapes. They are drawn in list order, with later shapes on top. Coordinates refer to a **1000 × 500** canvas. A wide TV banner can crop the top and bottom.

| Field | Meaning |
| --- | --- |
| `type` | `rect` for a rectangle, `ellipse` for an ellipse, or `polygon` for a shape made of points. |
| `color` | Fill color as `#RRGGBB`. |
| `x`, `y` | Rectangle or ellipse position: x from 0 to 1000, y from 0 to 500. |
| `width`, `height` | Rectangle or ellipse width from 1 to 1000 and height from 1 to 500. |
| `points` | For polygons, 3 to 40 points as `[[x,y], ...]`, within the same coordinate limits. |
| `opacity` | Optional opacity from 0 to 1. |
| `animation` | Optional object with `type` and `duration`. `move` moves back and forth, `blink` fades the shape, and `sway` rotates it through a fixed angle. Duration: 0.5–60 seconds. For `move`, optional `dx` and `dy` values between -300 and 300 set the displacement. |

Enable animations in the launcher settings. The template contains an example of each shape. Existing themes without `scene` remain compatible.

