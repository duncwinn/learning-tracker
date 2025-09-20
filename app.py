from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Data storage file
DATA_FILE = 'learning_data.json'

def load_data():
    """Load learning data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'courses': [], 'tags': []}

def save_data(data):
    """Save learning data to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_next_id(courses):
    """Get the next available ID for a new course"""
    if not courses:
        return 1
    return max(course['id'] for course in courses) + 1

@app.route('/')
def index():
    """Main page showing all courses"""
    data = load_data()
    courses = data.get('courses', [])
    tags = data.get('tags', [])
    
    # Filter courses by status for tabs
    todo_courses = [c for c in courses if c.get('status') == 'not_started']
    doing_courses = [c for c in courses if c.get('status') == 'in_progress']
    done_courses = [c for c in courses if c.get('status') == 'completed']
    
    return render_template('index.html', 
                         courses=courses, 
                         tags=tags,
                         todo_courses=todo_courses,
                         doing_courses=doing_courses,
                         done_courses=done_courses)

@app.route('/add_course', methods=['POST'])
def add_course():
    """Add a new course"""
    data = load_data()
    courses = data.get('courses', [])
    
    # Get tags from form (can be multiple)
    selected_tags = request.form.getlist('tags')
    
    new_course = {
        'id': get_next_id(courses),
        'title': request.form['title'],
        'description': request.form['description'],
        'status': request.form['status'],
        'tags': selected_tags,
        'links': [],
        'notes': [],
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    courses.append(new_course)
    data['courses'] = courses
    save_data(data)
    
    flash('Course added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/course/<int:course_id>')
def view_course(course_id):
    """View a specific course"""
    data = load_data()
    courses = data.get('courses', [])
    course = next((c for c in courses if c['id'] == course_id), None)
    
    if not course:
        flash('Course not found!', 'error')
        return redirect(url_for('index'))
    
    return render_template('course_detail.html', course=course)

@app.route('/add_link/<int:course_id>', methods=['POST'])
def add_link(course_id):
    """Add a link to a course"""
    data = load_data()
    courses = data.get('courses', [])
    course = next((c for c in courses if c['id'] == course_id), None)
    
    if course:
        new_link = {
            'id': len(course.get('links', [])) + 1,
            'title': request.form['link_title'],
            'url': request.form['link_url'],
            'description': request.form['link_description'],
            'added_at': datetime.now().isoformat()
        }
        
        if 'links' not in course:
            course['links'] = []
        course['links'].append(new_link)
        course['updated_at'] = datetime.now().isoformat()
        
        save_data(data)
        flash('Link added successfully!', 'success')
    
    return redirect(url_for('view_course', course_id=course_id))

@app.route('/add_note/<int:course_id>', methods=['POST'])
def add_note(course_id):
    """Add a note to a course"""
    data = load_data()
    courses = data.get('courses', [])
    course = next((c for c in courses if c['id'] == course_id), None)
    
    if course:
        new_note = {
            'id': len(course.get('notes', [])) + 1,
            'content': request.form['note_content'],
            'added_at': datetime.now().isoformat()
        }
        
        if 'notes' not in course:
            course['notes'] = []
        course['notes'].append(new_note)
        course['updated_at'] = datetime.now().isoformat()
        
        save_data(data)
        flash('Note added successfully!', 'success')
    
    return redirect(url_for('view_course', course_id=course_id))

@app.route('/update_status/<int:course_id>', methods=['POST'])
def update_status(course_id):
    """Update course status"""
    data = load_data()
    courses = data.get('courses', [])
    course = next((c for c in courses if c['id'] == course_id), None)
    
    if course:
        course['status'] = request.form['status']
        course['updated_at'] = datetime.now().isoformat()
        save_data(data)
        flash('Status updated successfully!', 'success')
    
    return redirect(url_for('view_course', course_id=course_id))

@app.route('/delete_course/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    """Delete a course"""
    data = load_data()
    courses = data.get('courses', [])
    courses = [c for c in courses if c['id'] != course_id]
    data['courses'] = courses
    save_data(data)
    
    flash('Course deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/add_tag', methods=['POST'])
def add_tag():
    """Add a new tag"""
    data = load_data()
    tags = data.get('tags', [])
    
    tag_name = request.form['tag_name'].strip()
    if tag_name and tag_name not in tags:
        tags.append(tag_name)
        data['tags'] = tags
        save_data(data)
        flash(f'Tag "{tag_name}" added successfully!', 'success')
    elif tag_name in tags:
        flash(f'Tag "{tag_name}" already exists!', 'error')
    else:
        flash('Tag name cannot be empty!', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete_tag', methods=['POST'])
def delete_tag():
    """Delete a tag"""
    data = load_data()
    tags = data.get('tags', [])
    courses = data.get('courses', [])
    
    tag_name = request.form['tag_name']
    
    if tag_name in tags:
        # Remove tag from all courses
        for course in courses:
            if tag_name in course.get('tags', []):
                course['tags'].remove(tag_name)
        
        # Remove tag from tags list
        tags.remove(tag_name)
        
        data['tags'] = tags
        data['courses'] = courses
        save_data(data)
        
        flash(f'Tag "{tag_name}" deleted successfully!', 'success')
    else:
        flash(f'Tag "{tag_name}" not found!', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
