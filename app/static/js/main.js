// AgroChemix Main JS

// Navbar scroll effect
const nav = document.getElementById('mainNav');
window.addEventListener('scroll', () => {
    nav?.classList.toggle('scrolled', window.scrollY > 60);
});

// Product category filter
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const cat = btn.dataset.category;
        document.querySelectorAll('.product-item').forEach(item => {
            item.style.display = (cat === 'all' || item.dataset.category === cat) ? '' : 'none';
        });
    });
});

// Contact form submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const btn = this.querySelector('button[type="submit"]');
        btn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
        btn.disabled = true;
        setTimeout(() => {
            btn.innerHTML = '<i class="fas fa-check me-2"></i>Message Sent!';
            btn.style.background = '#1A520D';
            contactForm.reset();
            setTimeout(() => {
                btn.innerHTML = '<i class="fas fa-paper-plane me-2"></i>Send Message';
                btn.disabled = false;
                btn.style.background = '';
            }, 3000);
        }, 1500);
    });
}

// Animate counters on home page
function animateCounters() {
    document.querySelectorAll('[data-count]').forEach(el => {
        const target = parseInt(el.dataset.count);
        const suffix = el.dataset.suffix || '';
        let current = 0;
        const step = target / 60;
        const interval = setInterval(() => {
            current = Math.min(current + step, target);
            el.textContent = Math.floor(current) + suffix;
            if (current >= target) clearInterval(interval);
        }, 25);
    });
}

// Intersection observer for counters
const statsEl = document.querySelector('.hero-stats');
if (statsEl) {
    const obs = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting) { animateCounters(); obs.disconnect(); }
    }, { threshold: 0.5 });
    obs.observe(statsEl);
}

// Scroll reveal
const revealEls = document.querySelectorAll('.product-card, .service-card, .value-card, .team-card, .testimonial-card, .feature-card');
const revealObs = new IntersectionObserver(entries => {
    entries.forEach((e, i) => {
        if (e.isIntersecting) {
            setTimeout(() => e.target.classList.add('revealed'), i * 80);
            revealObs.unobserve(e.target);
        }
    });
}, { threshold: 0.1 });

revealEls.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    revealObs.observe(el);
});

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.revealed, .product-card, .service-card, .value-card, .team-card, .testimonial-card, .feature-card').forEach(el => {
        el.addEventListener('transitionend', () => {});
    });
});

// Add revealed class styles via JS
const style = document.createElement('style');
style.textContent = '.revealed { opacity: 1 !important; transform: translateY(0) !important; }';
document.head.appendChild(style);