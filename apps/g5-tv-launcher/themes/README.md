# G5 TV Launcher themes

[English](README.md) · [Deutsch](README.de.md)

Download: [Spring](fruehling.json) · [Summer](sommer.json) · [Autumn](herbst.json) · [Winter](winter.json) · [Theme template](template.json)

The file importer and category selection are included in **0.2.70**. These examples were tested through the user's TV import flow; the exact appearance depends on the TV. This is an experimental format and may change in a future version.

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
| `image` | Optional background image as a `data:image/png;base64,...`, `data:image/jpeg;base64,...` or `data:image/webp;base64,...` data URL, at most 70,000 characters including the prefix. Omit it for a solid-color background. |

The complete file must be at most 80,000 bytes. Theme files contain data, not code: scripts, external URLs and SVG image data are not accepted. The current format changes colors and the background image, not the overall launcher layout or animations. Use original artwork or artwork you have permission to share; include attribution and license information when distributing it.

Example:

```json
{
  "format": "g5-theme",
  "version": 1,
  "id": "my-first-theme",
  "name": "My first theme",
  "background": "#102030",
  "accent": "#80d0ff",
  "glow": "#4466aa"
}
```
