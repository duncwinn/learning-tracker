// Learning Tracker JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    console.log('Learning Tracker JavaScript loaded');
    
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Auto-resize textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(function(textarea) {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    });

    // Auto-focus on first input in modals
    const modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
        modal.addEventListener('shown.bs.modal', function() {
            const firstInput = this.querySelector('input, textarea, select');
            if (firstInput) {
                firstInput.focus();
            }
        });
    });

    // Add hover effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Tag filtering functionality
    const tagFilter = document.getElementById('tagFilter');
    if (tagFilter) {
        tagFilter.addEventListener('change', function() {
            const selectedTag = this.value;
            const courseContainers = document.querySelectorAll('.course-card-container');
            
            courseContainers.forEach(function(container) {
                const courseTags = container.getAttribute('data-tags').split(',');
                
                if (selectedTag === '' || courseTags.includes(selectedTag)) {
                    container.style.display = 'block';
                } else {
                    container.style.display = 'none';
                }
            });
        });
    }

    // Tab switching with tag filter persistence
    const tabButtons = document.querySelectorAll('[data-bs-toggle="tab"]');
    tabButtons.forEach(function(button) {
        button.addEventListener('shown.bs.tab', function(e) {
            // Reapply tag filter when switching tabs
            const tagFilter = document.getElementById('tagFilter');
            if (tagFilter && tagFilter.value) {
                tagFilter.dispatchEvent(new Event('change'));
            }
        });
    });

    // Debug form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            console.log('Form submitted:', form.action);
            console.log('Form data:', new FormData(form));
        });
    });
});

// Utility functions
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        // Show success message
        const toast = document.createElement('div');
        toast.className = 'toast position-fixed top-0 end-0 m-3';
        toast.innerHTML = `
            <div class="toast-header">
                <i class="fas fa-check-circle text-success me-2"></i>
                <strong class="me-auto">Success</strong>
                <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
            </div>
            <div class="toast-body">
                Copied to clipboard!
            </div>
        `;
        document.body.appendChild(toast);
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        // Remove toast after it's hidden
        toast.addEventListener('hidden.bs.toast', function() {
            document.body.removeChild(toast);
        });
    });
}

// Search functionality (if needed in future)
function searchCourses(query) {
    const courses = document.querySelectorAll('.course-card');
    const searchTerm = query.toLowerCase();
    
    courses.forEach(function(course) {
        const title = course.querySelector('.card-title').textContent.toLowerCase();
        const description = course.querySelector('.card-text').textContent.toLowerCase();
        
        if (title.includes(searchTerm) || description.includes(searchTerm)) {
            course.style.display = 'block';
        } else {
            course.style.display = 'none';
        }
    });
}
