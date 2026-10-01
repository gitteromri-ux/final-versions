# Julie Masterclass page: mobile funnel and tracking audit, Oct 1 2026

**Page:** https://www.longevitylifeacademy.com/julie-masterclass/ (code at commit `1994ac7`, Sep 30 16:56 — latest deploy)
**Tested:** 9 devices × 2 plans = 18 full purchase runs: iPhone SE, iPhone 12 Mini, iPhone 14, iPhone 15 Pro Max, Galaxy S8, Galaxy A55, Pixel 7, iPad Mini, Desktop.
**No test leads in the CRM:** every call to the CRM worker, ActiveCampaign, the Meta relay, PayPal and Airwallex was intercepted and logged in the browser. Nothing reached a real server, so no lead, order, contact, event or charge was created.

## Verdict
**The funnel works end to end on every device and both plans.** Every button through to "Payment received" was clicked. All 5 Meta events fire on both Pixel and Conversions API with the same event ID (deduplication OK), correct values ($49 / $79), buyer email, phone, name and fbclid/fbc. The CRM order is created, the payment is reported to the CRM, and the success screen shows. No JavaScript errors.

## Issues, by urgency
1. **🔴 ActiveCampaign never receives "Purchased".** The page sends `LGV_Abandoned_Cart_Name_Details` → `Course_Details` → `No_Payment`, but never `LGV_Purchased`: the code handles that stage, but nothing ever triggers it (since Sep 23, commit f4407af). Unless the CRM/worker updates AC on payment server-side, **every buyer stays tagged "Abandoned cart – no payment" and can receive abandoned-cart emails after paying.** Check one real buyer in AC today. Fix: call `LLA_AC.send('LGV_Purchased')` after the payment report is accepted (card and PayPal).
2. **🟡 WhatsApp bubble covers the hero text** on small phones (iPhone SE / 12 Mini, Galaxy S8): it sits over the last words of the intro paragraph on the first screen.
3. **🟡 Checkout header is cramped on small phones:** the "Call Us +1-888-230-5110" line squeezes against the logo at 320–375 px.
4. **🟢 Plan buttons link to `#apply`, which doesn't exist.** They work (JavaScript opens checkout), but if a script fails to load the button does nothing. Point them at `#packages`.
5. **🟢 ActiveCampaign "Name details" stage is sent without the phone number** (it's added at the next stage). OK if intended.

## Tracking matrix (Pixel + CAPI both fired = ✅)
| Device | Plan | PageView | ViewContent | AddToCart | InitiateCheckout | Purchase | CRM order | Payment → CRM | Success screen | JS errors |
|---|---|---|---|---|---|---|---|---|---|---|
| iPhone SE | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| iPhone SE | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |
| iPhone 12 Mini | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| iPhone 12 Mini | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |
| iPhone 14 | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| iPhone 14 | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |
| iPhone 15 Pro Max | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| iPhone 15 Pro Max | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |
| Galaxy S8 | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| Galaxy S8 | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |
| Galaxy A55 | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| Galaxy A55 | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |
| Pixel 7 | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| Pixel 7 | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |
| iPad Mini | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| iPad Mini | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |
| Desktop Chrome | STANDARD | ✅ | ✅ | ✅ | ✅ | ✅ $49 | ✅ | ✅ | ✅ | 0 |
| Desktop Chrome | VIP | ✅ | ✅ | ✅ | ✅ | ✅ $79 | ✅ | ✅ | ✅ | 0 |

## Screenshots (step by step)
Flow: hero → plan card → step 1 → empty-form error → step 2 (plan & date) → card checkout → PayPal tab → payment received.

**iPhone SE (smallest iPhone), VIP**
![](sheet_iPhone_SE.jpg)

**Galaxy S8 (small Android), VIP**
![](sheet_Galaxy_S8.jpg)

**iPhone 15 Pro Max, VIP**
![](sheet_iPhone_15_Pro_Max.jpg)

Every device and plan has its own screenshots in [`shots/`](shots/) (01_hero … 10_after_purchase).

## Limits of this test (read before relying on it)
- **Browser engine:** devices were emulated in Chromium with real iPhone/Android screen sizes and user agents. That's not real Safari/WebKit. Do one real purchase on an iPhone before launch.
- **Payment forms:** the real Airwallex card form and PayPal button were replaced with stand-ins. The page's own logic was tested (amounts, order checks, Purchase firing, CRM report), but not the payment providers' own screens.
- **Fonts and images:** this environment can't reach the CodecPro font or the CloudFront images, so the screenshots show fallback fonts and some empty image slots. That's not a site bug.
