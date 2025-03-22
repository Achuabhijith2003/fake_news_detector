document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('news-form');
    const resultContainer = document.getElementById('result-container');
    
    // Add smooth animation when results appear
    if (resultContainer) {
        setTimeout(() => {
            resultContainer.style.opacity = '1';
            
            // Animate the confidence meter
            const meterFill = document.querySelector('.meter-fill');
            if (meterFill) {
                const targetWidth = meterFill.style.width;
                meterFill.style.width = '0%';
                setTimeout(() => {
                    meterFill.style.width = targetWidth;
                }, 300);
            }
        }, 100);
    }
    
    // Add form submission animation
    if (form) {
        form.addEventListener('submit', function() {
            const button = document.querySelector('.btn-analyze');
            button.textContent = 'Analyzing...';
            button.disabled = true;
            
            // If there's an existing result, fade it out
            if (resultContainer) {
                resultContainer.style.opacity = '0.5';
            }
        });
    }
});