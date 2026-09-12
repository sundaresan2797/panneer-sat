# Image drop-in guide

The real company logo and 6 real office/opening-ceremony photos are in
place (gallery). The hero and about sections still don't have a real photo
yet, so those show a styled placeholder (navy/blue gradient with the logo
watermark) instead of a broken image icon. Once supplied, drop new photos in
with these **exact filenames** and they will appear automatically — no
template changes needed.

```
static/images/               (served to visitors — everything here is deployed)
  logo/
    logo-nav.png             generated: trimmed + transparent, used in the navbar/footer/404/placeholders
    favicon-16.png, favicon-32.png, favicon-48.png   generated browser-tab icons
    apple-touch-icon.png     generated: 180x180, white background (iOS doesn't render transparency well)
  services/
    manpower.jpg, facility.jpg, transport.jpg, heavy-vehicle.jpg
      generated from design-source/Service/*.png — resized to 900px wide + JPEG-compressed (~100-160KB each)
      used on the "Our Services" cards on the homepage and /services page
  hero/
    hero.jpg                homepage hero image (actual vehicle / workforce / operation)
  company/
    company-01.jpg          used on the homepage "About" section
    og-cover.jpg            generated 1200x630 social-share image (logo + company name on navy) — replace with a real photo-based cover once available
  gallery/
    gallery-01.jpg ... gallery-06.jpg   real photos (office opening + pooja ceremony), shown on
                                          the homepage preview and the /gallery page. Metadata
                                          (alt text, category, crop focus) is in
                                          app/content/data.py -> GALLERY_PHOTOS, not the filename —
                                          add more by adding an entry there, in both "en" and "ta".
  vehicles/
    tipper-01.jpg ... tipper-04.jpg     heavy vehicle rental page
  manpower/, facility/, transport/      reserved for future use on service pages

design-source/               (project root — originals, NOT deployed to Vercel)
  company_logo.png           the real logo, as supplied
  Service/
    Manpower_Supply.png, Facility_Management.png,
    Transport_Logistics.png, Heavy_Vehicle_Rental.png   real photos as supplied (~2-3MB each)
  gallery/
    WhatsApp Image ....jpeg             the 6 original gallery photos, unrenamed/unprocessed
```

All 6 current gallery photos are tagged `"company"` (office opening / pooja
ceremony — there's no workforce, transport, or facility-management photo
yet). The `/gallery` page's category filter buttons for those still work,
they just show an empty grid until matching photos are added — that's
expected, not a bug.

Source files (the original logo and the full-resolution service photos) live
in `design-source/` at the project root, not under `static/images/`. That's
deliberate: `static/images/` is deployed as-is, so keeping multi-MB originals
out of it keeps the live site fast and the Vercel deployment small. Only the
generated, compressed, web-sized versions belong under `static/images/`.

If the service photos are ever replaced, drop the new files into
`design-source/Service/` using the same four names and regenerate
`static/images/services/*.jpg` the same way (resize to 900px wide, export as
JPEG ~82% quality).

If the logo is ever replaced, put the new file at
`design-source/company_logo.png` and regenerate the derived files
(`logo-nav.png`, the favicons, `apple-touch-icon.png`, `company/og-cover.jpg`)
the same way — trim the white margin, make the background transparent, then
export the sizes above — rather than editing them by hand.

See `BUSINESS_DETAILS_TO_CONFIRM.md` in the project root for the full list of
information (including the ~15–20 real photographs) still needed from the
business owner before this site is ready to launch.
