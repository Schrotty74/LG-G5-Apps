# webOS Homebrew IPK packaging

Applies to G5 TV Launcher, G5 System Monitor and future apps submitted to webosbrew/apps-repo.

- The IPK is an ar archive containing `debian-binary`, `control.tar.gz` and `data.tar.gz`.
- `control.tar.gz` must contain a regular file named exactly `control`, without a leading `./`.
- The control file must include `Package`, `Version`, `Architecture`, and `Installed-Size` in KiB. Use the installed files' total size rounded up to the next KiB.
- Use paths without a leading `./` in the data archive, including `usr/palm/applications/<app-id>/appinfo.json`. Match the app ID and version to `control`.
- Before submission, inspect both archives, verify the manifest URL, file size and SHA-256 against the actual IPK, and run the repository's validation. Test installation and functionality on a real TV separately.
- The System Monitor 0.9.3 package passed the PR metadata check after correcting `control` and adding `Installed-Size`. The separate compatibility check reported it could not run; a passing PR check does not replace a TV test.
- Do not replace an already released IPK with different bytes at the same URL. Publish a new version only when a release is explicitly requested.

The launcher's `build.py` implements the archive paths and computes `Installed-Size`. The System Monitor package 0.9.3 already contains these changes; apply these rules to its future build process too.
