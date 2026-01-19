document.addEventListener('DOMContentLoaded',()=>{
  const skills = document.querySelectorAll('.progress');
  const pcts = document.querySelectorAll('.pct');

  function animateSkills(){
    skills.forEach((el,i)=>{
      const p = +el.dataset.percent||0;
      const bar = el.querySelector('.bar');
      requestAnimationFrame(()=>{ bar.style.width = p + '%'; });
      // animate number
      const pctEl = pcts[i];
      if(pctEl){
        let cur=0; const target=p;
        const id = setInterval(()=>{ cur += Math.ceil(target/20); if(cur>=target){ cur=target; clearInterval(id);} pctEl.textContent = cur + '%'; },40);
      }
    });
  }

  // IntersectionObserver to trigger when visible
  const obs = new IntersectionObserver((entries,ob)=>{
    entries.forEach(ent=>{
      if(ent.isIntersecting){ animateSkills(); ob.disconnect(); }
    });
  },{threshold:0.25});

  const target = document.querySelector('#skills');
  if(target) obs.observe(target);
});
