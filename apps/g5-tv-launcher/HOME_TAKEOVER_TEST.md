# Direct Home takeover — test build

This is G5 TV Launcher test version 0.2.60, based on the earlier 0.2.50 release. Installing the IPK does not enable Home takeover or alter startup/key mappings.

## Using the test

1. In Glasshouse, select **Use LG Home** before testing this launcher. Glasshouse Home and this takeover cannot own LG Home together.
2. Install the test IPK and open **G5 TV Launcher** normally.
3. Open **Settings → Start & Home → TV Home screen**. Select **Direct Home takeover**, then **Apply method**. The confirmation authorizes the change on the TV.
4. Read the actual status. Success requires the mount, SAM's Home entry, the startup hook, the recovery monitor and an answer from the new page. The saved selection alone does not count as success.
5. Check Home from an HDMI input and from an app, the return after leaving an app, Favorites, Inputs, weather, language, settings, and restart/deep-standby behavior. Existing preferences are migrated to a private shared file on the TV, because the Home app has another identity.
6. To return, choose **LG Home** and apply. **Legacy method** enables our previous Magic Mapper Home mapping and legacy autostart; Magic Mapper 1.1.2 must be available and active for that method. The old individual controls remain available outside direct mode.

The switch restores our previous Home mapping using its existing backup, preserves other mapped keys, and disables our legacy autostart hook. An unrelated custom Home mapping, a missing backup, an unknown hook, or an active Glasshouse Home is refused instead of overwritten. If the saved previous Home mapping itself points elsewhere, resolve it in Magic Mapper before direct takeover. The mapper can remain installed for other keys.

## Recovery over SSH

If the page does not answer, the recovery monitor tries to return to LG Home. It checks only when LG Home is foreground, so opening a different app does not trigger recovery. A monitor is not a guarantee against every firmware or process failure. Keep this independent command available:

```sh
python3 /media/developer/apps/usr/palm/applications/org.schrotty74.g5launcher/home_mode_helper.py recover
```

This removes our direct startup hook, detaches only our overlay, releases/reloads LG's Home entry and opens LG Home. It refuses to unmount another app's overlay. An existing legacy Magic Mapper mapping is separate from this emergency recovery.

Always restore LG Home before uninstalling or upgrading this test build. The direct Home view is staged separately; an upgrade while it is mounted is not applied to that running view. Turn takeover off before upgrading, then re-enable it.

## Architecture and scope

- An original Python helper stages our UI under `/var/lib/webosbrew/g5-tv-launcher/home-mode/app`, with `com.webos.app.home`, `appCategory: ["home"]` and a vendor marker.
- A bind mount overlays `/usr/palm/applications/com.webos.app.home`; the LG files underneath are not rewritten. LG's layout/cache files are not blanked or edited.
- The helper asks SAM to reread only the Home app using block/release. Release is attempted even after a timed-out block. SAM is not restarted globally.
- Switching is journaled before system changes, uses an exclusive operation lock, and attempts rollback on failure. An interrupted transaction is not activated at boot; recovery is required.
- Preferences use atomic private JSON writes and remain compatible with the existing JSON backup contents. Importing a preferences backup does not activate Home takeover.
- A page heartbeat and separate recovery monitor are used. Direct Home accesses app data through a loopback-only token-protected bridge, not the denied Homebrew exec call. The bridge accepts fixed operations only; it does not execute arbitrary shell commands. A failed initial heartbeat causes rollback. Real TV testing is required.
- The local bridge binds only 127.0.0.1 and uses a random per-run token. Its app-list, icon, status and backup operations are allowlisted.
- The legacy helpers refuse activation while our direct mount is active. Foreign mounts, foreign startup hooks and active Glasshouse takeover are left alone.
- The installation paths are webOS platform paths, not paths to a developer's computer. No private TV state, keys, passwords or personal preferences are bundled.

## Validation performed

- 19 Home mode tests and 7 local bridge tests passed, using temporary files and mocked system/Luna operations: preference preservation, hook ownership, foreign takeover rejection, SAM release after timeout, manifest verification, mapper preservation, successful transition, failed transition and rollback/recovery.
- Python and JavaScript syntax checks passed.
- A test IPK was built and its archives inspected. These checks do not establish hardware functionality.
- A browser UI test was prepared but could not run here because the Chromium executable is unavailable. `test_ui.cjs` uses mocked service responses and requires a local Playwright/Chromium setup; it is not an app runtime dependency.
- The owner tested Direct Home on the TV, including a short standby and weather icon switching. A test after several hours of standby remains open.

## References

The approach was studied in Glasshouse's [home-takeover.js](https://github.com/rorygallagher2024/glasshouse/blob/main/server/lib/home-takeover.js), [samrescan.js](https://github.com/rorygallagher2024/glasshouse/blob/main/server/lib/samrescan.js) and [home.js](https://github.com/rorygallagher2024/glasshouse/blob/main/server/lib/home.js). Our implementation is independent and does not depend on Glasshouse's server or copy its source modules.

Build with `python3 build.py`. Run the host-side tests with `python3 test_home_mode.py`. The test package uses version 0.2.60 and is separate from the published 0.2.50 package.
