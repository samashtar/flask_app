window.addEventListener("DOMContentLoaded", () => {
  checkFileName();
  document
    .getElementById("file-upload")
    .addEventListener("change", updateFileName);

  document
    .getElementById("submit-button")
    .addEventListener("click", submitEmpty);
});

//updates input label
function updateFileName(event) {
  const input = event.target;
  if ("files" in input && input.files.length > 0) {
    const fileName = document.getElementById("file-name");
    fileName.innerText = input.files[0].name;
  }
}

// stops empty submits
function submitEmpty(event) {
  const fileName = document.getElementById("file-name");
  if (fileName.innerText === "Upload an Image") {
    event.preventDefault();
    alert("Please upload an image first");
  }
}

//checks for existing input name if the user goes back
function checkFileName() {
  const fileName = document.getElementById("file-name");
  const fileInput = document.getElementById("file-upload");
  if (fileInput.value !== "") {
    fileName.innerText = fileInput.value.replace(/^C:\\fakepath\\/i, "");
  }
}
