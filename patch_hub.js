function copyText(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(showToast);
    } else {
        let ta = document.createElement("textarea");
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
        showToast();
    }
}
function showToast() {
    let toast = document.getElementById("toast");
    toast.className = "show";
    setTimeout(() => toast.className = toast.className.replace("show", ""), 3000);
}
