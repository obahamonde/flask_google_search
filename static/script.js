const el = document.getElementById("google-search");
el.addEventListener("keyup", async (e) => {
  if (e.key === "Enter") {
    const res = await fetch(`/${el.value}`, { method: "POST" });
    const data = await res.json();
    data.forEach((item) => {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = item.link;
      a.target = "_blank";
      a.innerText = item.title;
      a.classList.add("result");
      li.appendChild(a);
      li.style.listStyle = "none";
      li.style.margin = "0.4rem";
      document.querySelector("ul").appendChild(li);
    });
  }
else if (e.key === "Backspace") {
    document.querySelector("ul").innerHTML = "";
  }
});
