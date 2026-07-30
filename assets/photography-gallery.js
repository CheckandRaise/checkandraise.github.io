(() => {
  const dialog = document.querySelector("#photo-lightbox");
  const triggers = Array.from(document.querySelectorAll(".photo-open"));

  if (!dialog || triggers.length === 0) {
    return;
  }

  const image = dialog.querySelector(".photo-lightbox-image");
  const closeButton = dialog.querySelector(".photo-lightbox-close");
  const previousButton = dialog.querySelector(".photo-lightbox-prev");
  const nextButton = dialog.querySelector(".photo-lightbox-next");
  const fields = {
    location: dialog.querySelector(".photo-lightbox-location"),
    caption: dialog.querySelector(".photo-lightbox-caption"),
    date: dialog.querySelector(".photo-lightbox-date"),
    camera: dialog.querySelector(".photo-lightbox-camera"),
    lens: dialog.querySelector(".photo-lightbox-lens"),
    focal: dialog.querySelector(".photo-lightbox-focal"),
    aperture: dialog.querySelector(".photo-lightbox-aperture"),
    shutter: dialog.querySelector(".photo-lightbox-shutter"),
    iso: dialog.querySelector(".photo-lightbox-iso"),
    count: dialog.querySelector(".photo-lightbox-count"),
  };
  let currentIndex = 0;

  const render = (index) => {
    currentIndex = (index + triggers.length) % triggers.length;
    const data = triggers[currentIndex].dataset;

    image.src = data.full;
    image.alt = data.alt;
    fields.location.textContent = data.location;
    fields.caption.textContent = data.caption;
    fields.date.textContent = data.date;
    fields.camera.textContent = data.camera;
    fields.lens.textContent = data.lens;
    fields.focal.textContent = data.focal;
    fields.aperture.textContent = data.aperture;
    fields.shutter.textContent = data.shutter;
    fields.iso.textContent = data.iso;
    fields.count.textContent = `${currentIndex + 1} / ${triggers.length}`;
  };

  const open = (index) => {
    render(index);
    document.body.classList.add("photo-lightbox-open");

    if (typeof dialog.showModal === "function") {
      dialog.showModal();
    } else {
      dialog.setAttribute("open", "");
      dialog.classList.add("photo-lightbox-fallback");
    }

    closeButton.focus();
  };

  const close = () => {
    if (typeof dialog.close === "function") {
      dialog.close();
    } else {
      dialog.removeAttribute("open");
    }

    dialog.classList.remove("photo-lightbox-fallback");
    document.body.classList.remove("photo-lightbox-open");
    image.removeAttribute("src");
    triggers[currentIndex].focus();
  };

  triggers.forEach((trigger, index) => {
    trigger.addEventListener("click", () => open(index));
  });

  closeButton.addEventListener("click", close);
  previousButton.addEventListener("click", () => render(currentIndex - 1));
  nextButton.addEventListener("click", () => render(currentIndex + 1));

  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      close();
    }
  });

  dialog.addEventListener("close", () => {
    document.body.classList.remove("photo-lightbox-open");
    image.removeAttribute("src");
  });

  document.addEventListener("keydown", (event) => {
    if (!dialog.hasAttribute("open")) {
      return;
    }

    if (event.key === "ArrowLeft") {
      render(currentIndex - 1);
    } else if (event.key === "ArrowRight") {
      render(currentIndex + 1);
    } else if (event.key === "Escape" && typeof dialog.close !== "function") {
      close();
    }
  });
})();
