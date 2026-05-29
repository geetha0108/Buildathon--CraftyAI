---
name: Craft & Cozy
colors:
  surface: '#fbf9f1'
  surface-dim: '#dcdad2'
  surface-bright: '#fbf9f1'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f4ec'
  surface-container: '#f0eee6'
  surface-container-high: '#eae8e0'
  surface-container-highest: '#e4e3db'
  on-surface: '#1b1c17'
  on-surface-variant: '#404848'
  inverse-surface: '#30312c'
  inverse-on-surface: '#f3f1e9'
  outline: '#707979'
  outline-variant: '#c0c8c8'
  surface-tint: '#356668'
  primary: '#356668'
  on-primary: '#ffffff'
  primary-container: '#a8dadc'
  on-primary-container: '#306163'
  inverse-primary: '#9ecfd1'
  secondary: '#6c586d'
  on-secondary: '#ffffff'
  secondary-container: '#f5daf4'
  on-secondary-container: '#725e73'
  tertiary: '#74593f'
  on-tertiary: '#ffffff'
  tertiary-container: '#eecaaa'
  on-tertiary-container: '#6e543a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b9ecee'
  primary-fixed-dim: '#9ecfd1'
  on-primary-fixed: '#002021'
  on-primary-fixed-variant: '#1a4e50'
  secondary-fixed: '#f5daf4'
  secondary-fixed-dim: '#d8bfd8'
  on-secondary-fixed: '#251628'
  on-secondary-fixed-variant: '#534155'
  tertiary-fixed: '#ffdcbe'
  tertiary-fixed-dim: '#e3c0a0'
  on-tertiary-fixed: '#2a1704'
  on-tertiary-fixed-variant: '#5a422a'
  background: '#fbf9f1'
  on-background: '#1b1c17'
  surface-variant: '#e4e3db'
typography:
  headline-lg:
    fontFamily: Literata
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Literata
    fontSize: 30px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Literata
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Literata
    fontSize: 22px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Quicksand
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.6'
  body-md:
    fontFamily: Quicksand
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.6'
  label-md:
    fontFamily: Quicksand
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Quicksand
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  card-padding: 24px
---

## Brand & Style
The design system is built to evoke the warmth of a handmade gift and the tactile satisfaction of textile arts. It targets a creative audience of crafters, hobbyists, and small business owners who value authenticity and patience. 

The aesthetic is a blend of **Tactile Skeuomorphism** and **Minimalism**. It uses soft, "squishy" UI elements that feel touchable, paired with generous whitespace to ensure the interface remains functional and breathable. The goal is to make the user feel like they are stepping into a sun-drenched craft room: organized, inspiring, and deeply personal.

## Colors
The palette is derived from natural dyed yarns and pastel fibers.
- **Primary (Soft Mint):** Used for main actions and success states, providing a refreshing, calm focal point.
- **Secondary (Lavender):** Used for accents, secondary buttons, and category indicators.
- **Tertiary (Peach):** Used for highlights, notifications, and "save" actions to provide a warm, energetic contrast.
- **Neutral (Cream):** The foundation of the UI. Avoid pure white (#FFFFFF); use the cream base for all surfaces to maintain the "handmade paper" or "raw cotton" feel.

## Typography
The typography strategy pairs the intellectual, cozy reliability of a serif with the modern, approachable friendliness of a rounded sans-serif. 

**Literata** serves as the voice of the brand, used for titles and storytelling to give the UI a "published" and academic craft feel. **Quicksand** handles all functional UI tasks—navigation, buttons, and form labels—ensuring that even dense information feels soft and accessible. Use "Medium" (500) as the default weight for body text to maintain legibility against pastel backgrounds.

## Layout & Spacing
This design system utilizes a **Fixed Grid** for desktop (1200px max-width) and a **Fluid Grid** for mobile. The layout is heavily card-based, mimicking swatches of fabric or pattern cards.

- **Desktop:** 12-column grid with 24px gutters. Content is centered with wide 64px margins to create a "scrapbook" frame.
- **Mobile:** 4-column grid with 16px margins.
- **Rhythm:** Use an 8px base unit. All internal component padding should be multiples of 8. For sections, use larger 48px or 64px gaps to emphasize the minimalist, unhurried brand personality.

## Elevation & Depth
Depth is created through **Ambient Shadows** rather than high-contrast light sources.
- **Surface Layer:** The Cream background (#FFFDF5) acts as the floor.
- **Card Layer:** Cards use a very soft, diffused shadow with a hint of the secondary color (Lavender) in the shadow tint. Example: `box-shadow: 0 8px 30px rgba(216, 191, 216, 0.2);`.
- **Active State:** When interacting with buttons or cards, they should appear to "sink" into the surface (reduce shadow Y-offset and blur) rather than lifting off, simulating the squishiness of wool or fabric.
- **Texture:** Apply a subtle, low-opacity (2-3%) noise or "linen" pattern overlay to the primary containers to give a tactile yarn-like appearance.

## Shapes
The shape language is defined by extreme softness. There are no sharp corners in this design system. 
- **Small Components:** Buttons and input fields use full pill-shaping (rounded-full).
- **Containers:** Large cards and modals use the `rounded-xl` (1.5rem / 24px) or `rounded-2xl` (2rem / 32px) settings to mimic the organic curves of knitted loops.
- **Icons:** Icons should have rounded caps and corners, with a consistent 2px stroke weight.

## Components
- **Buttons:** Use high-contrast pill shapes. The primary button should have a "bouncy" hover transition (transform: scale(1.03)). 
- **Cards:** Cards are the primary vessel for content. They feature a 1px solid border in a slightly darker shade of the neutral color (#F0EAD6) to define edges without adding harshness.
- **Chips:** Used for "Yarn Weight" or "Skill Level." These should look like small stitched labels, using the Secondary or Tertiary colors with Quicksand Bold.
- **Input Fields:** Fields are Cream-colored with a Soft Mint border on focus. Use a 16px internal padding to ensure the text doesn't feel cramped.
- **Progress Indicators:** For crochet patterns or tutorials, use a custom progress bar that looks like a growing chain-stitch or a line of yarn.
- **Checkboxes:** Replace standard square boxes with circular "button-style" toggles that feel more like physical sewing buttons.