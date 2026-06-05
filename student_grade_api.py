# Student Grade API - REST API for Grade Calculation

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to assign grade based on average
def assign_grade(average):
    if average >= 95:
        return "A+"
    elif average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

@app.route('/')
def index():
    return render_template('api_input.html')

@app.route('/api/calculate-grades', methods=['POST'])
def api_calculate_grades():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data or 'students' not in data:
            return jsonify({'error': 'Invalid request. Please provide students data.'}), 400
        
        students_data = data['students']
        results = []
        
        for student_data in students_data:
            marks = student_data.get('marks')
            if marks is None:
                return jsonify({'error': 'Marks are required for each student'}), 400
            
            grade = assign_grade(marks)
            results.append({
                'name': student_data.get('name', 'ALIA'),
                'marks': marks,
                'grade': grade
            })
        
        return jsonify({
            'success': True,
            'students': results
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'Student Grade API'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
