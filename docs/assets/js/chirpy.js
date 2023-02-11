const mkDocsChirpyTranslator = {
  default: "light",
  slate: "dark",
};

const mkDocs = document.querySelector("[data-md-color-scheme]");
const chirpy = document.querySelector("[data-chirpy-theme]");

if (chirpy) {
  //if mkdocs attribute at the first chargement is light, switch to light directly
  if (mkDocs.getAttribute("data-md-color-scheme") === "default") {
    chirpy.setAttribute("data-chirpy-theme", "light");
  }

  // create mutation observer to change chirpyTheme when mkDocs theme changes
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.type === "attributes") {
        chirpy.setAttribute(
          "data-chirpy-theme",
          mkDocsChirpyTranslator[mkDocs.dataset.mdColorScheme]
        );
      }
    });
  });

  // observe mkDocs theme change
  observer.observe(mkDocs, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  });
}
