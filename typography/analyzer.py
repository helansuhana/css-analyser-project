from playwright.sync_api import sync_playwright


def analyze_website(url):

    layout = set()
    typography = set()
    colors = set()
    box = set()
    flex = set()
    animation = set()

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        elements = page.query_selector_all("*")

        for element in elements:

            try:

                styles = page.evaluate(
                    """(el) => {
                        const s = window.getComputedStyle(el);
                        return {
                            display:s.display,
                            position:s.position,
                            width:s.width,
                            height:s.height,
                            margin:s.margin,
                            padding:s.padding,
                            border:s.border,

                            fontFamily:s.fontFamily,
                            fontSize:s.fontSize,
                            fontWeight:s.fontWeight,
                            textAlign:s.textAlign,
                            lineHeight:s.lineHeight,

                            color:s.color,
                            backgroundColor:s.backgroundColor,
                            opacity:s.opacity,

                            borderRadius:s.borderRadius,
                            boxShadow:s.boxShadow,

                            flexDirection:s.flexDirection,
                            justifyContent:s.justifyContent,
                            alignItems:s.alignItems,

                            transform:s.transform,
                            transition:s.transitionProperty,
                            animation:s.animationName
                        };
                    }""",
                    element
                )

                # Layout
                layout.add(f"display: {styles['display']}")
                layout.add(f"position: {styles['position']}")
                layout.add(f"width: {styles['width']}")
                layout.add(f"height: {styles['height']}")
                layout.add(f"margin: {styles['margin']}")
                layout.add(f"padding: {styles['padding']}")
                layout.add(f"border: {styles['border']}")

                # Typography
                typography.add(f"font-family: {styles['fontFamily']}")
                typography.add(f"font-size: {styles['fontSize']}")
                typography.add(f"font-weight: {styles['fontWeight']}")
                typography.add(f"text-align: {styles['textAlign']}")
                typography.add(f"line-height: {styles['lineHeight']}")

                # Colors
                colors.add(f"color: {styles['color']}")
                colors.add(f"background-color: {styles['backgroundColor']}")
                colors.add(f"opacity: {styles['opacity']}")

                # Box model
                box.add(f"border-radius: {styles['borderRadius']}")
                box.add(f"box-shadow: {styles['boxShadow']}")

                # Flex/Grid
                flex.add(f"flex-direction: {styles['flexDirection']}")
                flex.add(f"justify-content: {styles['justifyContent']}")
                flex.add(f"align-items: {styles['alignItems']}")

                # Animation
                animation.add(f"transform: {styles['transform']}")
                animation.add(f"transition: {styles['transition']}")
                animation.add(f"animation: {styles['animation']}")

            except:
                pass

        browser.close()

    return {
        "layout": sorted(layout),
        "typography": sorted(typography),
        "colors": sorted(colors),
        "box": sorted(box),
        "flex": sorted(flex),
        "animation": sorted(animation)
    }


