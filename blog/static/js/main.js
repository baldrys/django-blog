const idOfImageInput = "id_image";
const idOfImageSrc = "id_image_show";
const closeIcon = document.querySelector(".article-create__image-close");
const output = document.getElementById("id_image_show");
const inputImgFile = document.getElementById("id_image");
const buttonUpload = document.getElementById("btn-upload-img");

var loadFile = function (event) {
	output.src = URL.createObjectURL(event.target.files[0]);

	output.onload = function () {
		URL.revokeObjectURL(output.src); // free memory

		buttonUpload.style.display = "none";
		closeIcon.style.display = "block";
		output.style.display = "inline";
	};
};

var removeImg = function (event) {
	buttonUpload.style.display = "block";
	closeIcon.style.display = "none";
	output.style.display = "none";
	inputImgFile.form.reset();
};

closeIcon.addEventListener("click", removeImg);
inputImgFile.addEventListener("change", loadFile);
