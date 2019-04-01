window.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("file-upload")
    .addEventListener("change", getFileName);
});

function readFileContent(file) {
  debugger;
  const reader = new FileReader();
  return new Promise((resolve, reject) => {
    reader.onload = event => resolve(event.target.result);
    reader.onerror = error => reject(error);
    reader.readAsText(file);
  });
}

function getFileName(event) {
  debugger;
  const input = event.target;
  if ("file" in input && input.files.length > 0) {
    placeFileContent(document.getElementById("content-target"), input.files[0]);
  }
}

function placeFileContent(target, file) {
  debugger;
  readFileContent(file)
    .then(content => {
      target.value = content;
    })
    .catch(error => console.log(error));
}
