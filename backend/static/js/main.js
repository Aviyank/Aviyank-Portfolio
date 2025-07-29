// Main JavaScript file for AI-Enhanced Portfolio

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initAnimations();
    initTooltips();
    initFormValidation();
    initAIServices();
    initSmoothScrolling();
    initNavbarEffects();
});

// Animation on scroll
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll('.card, .skill-item, .ai-service-card');
    animateElements.forEach(el => observer.observe(el));
}

// Initialize Bootstrap tooltips
function initTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Form validation
function initFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

// AI Services functionality
function initAIServices() {
    // Sentiment Analysis
    const sentimentForm = document.getElementById('sentiment-form');
    if (sentimentForm) {
        sentimentForm.addEventListener('submit', handleSentimentAnalysis);
    }

    // Text Generation
    const textGenForm = document.getElementById('text-generation-form');
    if (textGenForm) {
        textGenForm.addEventListener('submit', handleTextGeneration);
    }

    // Data Analysis
    const dataAnalysisForm = document.getElementById('data-analysis-form');
    if (dataAnalysisForm) {
        dataAnalysisForm.addEventListener('submit', handleDataAnalysis);
    }
}

// Handle Sentiment Analysis
async function handleSentimentAnalysis(event) {
    event.preventDefault();
    
    const form = event.target;
    const textInput = form.querySelector('#text-input');
    const resultDiv = document.getElementById('sentiment-result');
    const loadingDiv = document.getElementById('sentiment-loading');
    
    if (!textInput.value.trim()) {
        showAlert('Please enter some text to analyze.', 'warning');
        return;
    }
    
    // Show loading
    if (loadingDiv) loadingDiv.style.display = 'block';
    if (resultDiv) resultDiv.style.display = 'none';
    
    try {
        const response = await fetch('/api/sentiment/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                text: textInput.value.trim()
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            displaySentimentResult(data);
        } else {
            showAlert(data.error || 'An error occurred during analysis.', 'danger');
        }
    } catch (error) {
        showAlert('Network error. Please try again.', 'danger');
    } finally {
        if (loadingDiv) loadingDiv.style.display = 'none';
    }
}

// Display Sentiment Analysis Result
function displaySentimentResult(data) {
    const resultDiv = document.getElementById('sentiment-result');
    if (!resultDiv) return;
    
    const sentimentClass = data.sentiment === 'positive' ? 'sentiment-positive' : 
                          data.sentiment === 'negative' ? 'sentiment-negative' : 'sentiment-neutral';
    
    resultDiv.innerHTML = `
        <div class="ai-result">
            <h5>Analysis Results</h5>
            <div class="row">
                <div class="col-md-6">
                    <p><strong>Sentiment:</strong> <span class="${sentimentClass}">${data.sentiment.charAt(0).toUpperCase() + data.sentiment.slice(1)}</span></p>
                    <p><strong>Confidence:</strong> ${(data.confidence * 100).toFixed(1)}%</p>
                    <p><strong>Polarity:</strong> ${data.polarity.toFixed(3)}</p>
                    <p><strong>Subjectivity:</strong> ${data.subjectivity.toFixed(3)}</p>
                </div>
                <div class="col-md-6">
                    <p><strong>Keywords:</strong></p>
                    <div class="keywords-container">
                        ${data.keywords.map(keyword => `<span class="badge bg-secondary me-1">${keyword}</span>`).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;
    
    resultDiv.style.display = 'block';
}

// Handle Text Generation
async function handleTextGeneration(event) {
    event.preventDefault();
    
    const form = event.target;
    const promptInput = form.querySelector('#prompt-input');
    const maxTokensInput = form.querySelector('#max-tokens');
    const temperatureInput = form.querySelector('#temperature');
    const resultDiv = document.getElementById('text-generation-result');
    const loadingDiv = document.getElementById('text-generation-loading');
    
    if (!promptInput.value.trim()) {
        showAlert('Please enter a prompt for text generation.', 'warning');
        return;
    }
    
    // Show loading
    if (loadingDiv) loadingDiv.style.display = 'block';
    if (resultDiv) resultDiv.style.display = 'none';
    
    try {
        const response = await fetch('/api/text-generation/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                prompt: promptInput.value.trim(),
                max_tokens: parseInt(maxTokensInput.value) || 100,
                temperature: parseFloat(temperatureInput.value) || 0.7
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            displayTextGenerationResult(data);
        } else {
            showAlert(data.error || 'An error occurred during text generation.', 'danger');
        }
    } catch (error) {
        showAlert('Network error. Please try again.', 'danger');
    } finally {
        if (loadingDiv) loadingDiv.style.display = 'none';
    }
}

// Display Text Generation Result
function displayTextGenerationResult(data) {
    const resultDiv = document.getElementById('text-generation-result');
    if (!resultDiv) return;
    
    resultDiv.innerHTML = `
        <div class="ai-result">
            <h5>Generated Text</h5>
            <div class="mb-3">
                <strong>Model:</strong> ${data.model_used}
            </div>
            <div class="mb-3">
                <strong>Generated Text:</strong>
                <div class="mt-2 p-3 bg-light rounded">
                    ${data.generated_text.replace(/\n/g, '<br>')}
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <strong>Parameters:</strong>
                    <ul class="list-unstyled">
                        <li>Max Tokens: ${data.parameters.max_tokens}</li>
                        <li>Temperature: ${data.parameters.temperature}</li>
                    </ul>
                </div>
            </div>
        </div>
    `;
    
    resultDiv.style.display = 'block';
}

// Handle Data Analysis
async function handleDataAnalysis(event) {
    event.preventDefault();
    
    const form = event.target;
    const dataInput = form.querySelector('#data-input');
    const analysisTypeSelect = form.querySelector('#analysis-type');
    const resultDiv = document.getElementById('data-analysis-result');
    const loadingDiv = document.getElementById('data-analysis-loading');
    
    if (!dataInput.value.trim()) {
        showAlert('Please enter data for analysis.', 'warning');
        return;
    }
    
    // Show loading
    if (loadingDiv) loadingDiv.style.display = 'block';
    if (resultDiv) resultDiv.style.display = 'none';
    
    try {
        let data;
        try {
            data = JSON.parse(dataInput.value.trim());
        } catch (e) {
            showAlert('Please enter valid JSON data.', 'warning');
            return;
        }
        
        const response = await fetch('/api/data-analysis/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({
                data: data,
                analysis_type: analysisTypeSelect.value
            })
        });
        
        const responseData = await response.json();
        
        if (response.ok) {
            displayDataAnalysisResult(responseData);
        } else {
            showAlert(responseData.error || 'An error occurred during data analysis.', 'danger');
        }
    } catch (error) {
        showAlert('Network error. Please try again.', 'danger');
    } finally {
        if (loadingDiv) loadingDiv.style.display = 'none';
    }
}

// Display Data Analysis Result
function displayDataAnalysisResult(data) {
    const resultDiv = document.getElementById('data-analysis-result');
    if (!resultDiv) return;
    
    let insightsHtml = '';
    if (data.insights && data.insights.length > 0) {
        insightsHtml = `
            <div class="mb-3">
                <strong>Key Insights:</strong>
                <ul>
                    ${data.insights.map(insight => `<li>${insight}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    resultDiv.innerHTML = `
        <div class="ai-result">
            <h5>${data.analysis_type.charAt(0).toUpperCase() + data.analysis_type.slice(1)} Analysis Results</h5>
            ${insightsHtml}
            <div class="mb-3">
                <strong>Analysis Type:</strong> ${data.analysis_type}
            </div>
            <div class="mb-3">
                <strong>Results Summary:</strong>
                <pre class="bg-light p-3 rounded"><code>${JSON.stringify(data.results, null, 2)}</code></pre>
            </div>
        </div>
    `;
    
    resultDiv.style.display = 'block';
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Navbar effects
function initNavbarEffects() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
}

// Utility functions
function getCSRFToken() {
    const token = document.querySelector('meta[name="csrf-token"]');
    return token ? token.getAttribute('content') : '';
}

function showAlert(message, type = 'info') {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type} alert-dismissible fade show`;
    alertContainer.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alertContainer, container.firstChild);
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (alertContainer.parentNode) {
                alertContainer.remove();
            }
        }, 5000);
    }
}

// Copy to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showAlert('Copied to clipboard!', 'success');
    }).catch(function() {
        showAlert('Failed to copy to clipboard.', 'danger');
    });
}

// Add copy buttons to code blocks
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('pre code').forEach(block => {
        const copyButton = document.createElement('button');
        copyButton.className = 'btn btn-sm btn-outline-secondary copy-btn';
        copyButton.innerHTML = '<i class="fas fa-copy"></i>';
        copyButton.onclick = () => copyToClipboard(block.textContent);
        
        block.parentNode.style.position = 'relative';
        block.parentNode.appendChild(copyButton);
    });
});

// Lazy loading for images
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Initialize lazy loading
initLazyLoading();

// Add CSS for navbar scroll effect
const style = document.createElement('style');
style.textContent = `
    .navbar-scrolled {
        background: rgba(52, 58, 64, 0.95) !important;
        backdrop-filter: blur(10px);
    }
    
    .copy-btn {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 10;
    }
    
    .lazy {
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .lazy.loaded {
        opacity: 1;
    }
`;
document.head.appendChild(style); 