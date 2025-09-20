# 🎓 Learning Tracker

A modern web application built with Flask for tracking your learning courses, links, and notes. Perfect for students, professionals, and lifelong learners who want to organize their educational journey.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 📚 **Course Management**: Create and manage learning courses with titles, descriptions, and status tracking
- 🏷️ **Tag System**: Organize courses with custom tags for better categorization
- 📊 **Progress Tracking**: Three main tabs - ToDo, Doing, Done - for clear progress visualization
- 🔗 **Link & Reference Storage**: Save important links and references for each course
- 📝 **Note Taking**: Add and organize notes for each course
- 🎨 **Modern UI**: Beautiful, responsive design built with Bootstrap 5
- 📱 **Mobile Friendly**: Works perfectly on desktop, tablet, and mobile devices
- 🔍 **Smart Filtering**: Filter courses by tags across all status tabs

## Installation

1. **Clone or download this repository**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://localhost:5001`

## Usage

### Adding a New Course
1. Click the "Add New Course" button on the home page
2. Fill in the course title, description, and initial status
3. Click "Add Course" to save

### Managing Course Content
1. Click "View" on any course card to open the course detail page
2. Add links and references using the "Add Link" button
3. Add notes using the "Add Note" button
4. Update course status using the status dropdown

### Course Status Options
- **Not Started**: Course hasn't been begun yet
- **In Progress**: Currently working on the course
- **Completed**: Course has been finished

## File Structure

```
myfirstpy/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── learning_data.json    # Data storage (created automatically)
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   └── course_detail.html # Course detail page
└── static/               # Static assets
    ├── css/
    │   └── style.css     # Custom styles
    └── js/
        └── main.js       # JavaScript functionality
```

## Data Storage

The application uses JSON files for data storage, making it easy to backup and transfer your learning data. The data is stored in `learning_data.json` in the application directory.

## Customization

### Styling
- Modify `static/css/style.css` to customize the appearance
- The app uses Bootstrap 5, so you can leverage Bootstrap classes and components

### Functionality
- Add new features by modifying `app.py` and the corresponding templates
- JavaScript functionality can be extended in `static/js/main.js`

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this learning tracker!

---

**Happy Learning!** 🎓
