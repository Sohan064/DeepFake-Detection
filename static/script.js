document.getElementById("image").onchange = (event) => {
    const file = event.target.files[0];
    const preview = document.getElementById("preview");

    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            preview.src = e.target.result;
            preview.style.display = "block";
        };
        reader.readAsDataURL(file);
    } else {
        preview.src = "";
        preview.style.display = "none";
    }
};

document.getElementById("upload-form").onsubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const resultText = await response.text();
    document.getElementById("result").textContent = resultText;
};
