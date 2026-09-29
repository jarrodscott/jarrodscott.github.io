document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".telemetry-card");

  cards.forEach(card => {
    card.addEventListener("mouseenter", () => {
      const siteId = card.getAttribute("data-site-id");
      const targetPin = document.querySelector(`[data-pin-id="${siteId}"]`);
      
      if (targetPin) {
        const dot = targetPin.querySelector(".node-center-dot");
        
        document.querySelectorAll(".node-center-dot").forEach(el => {
          el.classList.remove("pin-highlight-active");
        });

        if (dot) {
          dot.classList.add("pin-highlight-active");
        }
      }
    });

    card.addEventListener("mouseleave", () => {
      const siteId = card.getAttribute("data-site-id");
      const targetPin = document.querySelector(`[data-pin-id="${siteId}"]`);
      
      if (targetPin) {
        const dot = targetPin.querySelector(".node-center-dot");
        if (dot) {
          dot.classList.remove("pin-highlight-active");
        }
      }
    });
  });

  // Pin Click Logic Engine
  const pins = document.querySelectorAll(".research-map-hotspot-node");

  pins.forEach(pin => {
    // 1. Handle clicking the pin itself to open or target links
    pin.addEventListener("click", (e) => {
      // If clicking the close button, execute closure and bypass the rest
      if (e.target.classList.contains("tooltip-close-btn")) {
        e.stopPropagation();
        pin.classList.remove("tooltip-active");
        return;
      }

      // If clicking the link itself, allow browser execution behavior
      if (e.target.tagName === 'A' || e.target.closest('a')) {
        return;
      }

      e.stopPropagation();
      const isAlreadyOpen = pin.classList.contains("tooltip-active");

      // Reset all instances
      document.querySelectorAll(".research-map-hotspot-node").forEach(p => {
        p.classList.remove("tooltip-active");
      });

      // Toggle current target
      if (!isAlreadyOpen) {
        pin.classList.add("tooltip-active");
      }
    });
  });


  // Global dismiss listener
  document.addEventListener("click", () => {
    document.querySelectorAll(".research-map-hotspot-node").forEach(p => {
      p.classList.remove("tooltip-active");
    });
  });
});
