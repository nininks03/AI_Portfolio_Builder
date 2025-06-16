from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from ai import call_google_ai_model


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False)
    subject= db.Column(db.String(100), nullable=False)
    message= db.Column(db.String(100), nullable=False)


class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String(255), nullable=False)
    program_name_1 = db.Column(db.String(100), nullable=False)
    program_1_university = db.Column(db.String(100), nullable=False)
    program1_year = db.Column(db.String(50), nullable=False)
    program1_skills = db.Column(db.Text, nullable=False)
    program_name_2 = db.Column(db.String(100), nullable=False)
    program_2_university = db.Column(db.String(100), nullable=False)
    program2_year = db.Column(db.String(50), nullable=False)
    program2_skills = db.Column(db.Text, nullable=False)
    project1_name = db.Column(db.String(100), nullable=False)
    project1_description = db.Column(db.Text, nullable=False)
    project1_skills = db.Column(db.Text, nullable=False)
    project2_name = db.Column(db.String(100), nullable=False)
    project2_description = db.Column(db.Text, nullable=False)
    project2_skills = db.Column(db.Text, nullable=False)
    project3_name = db.Column(db.String(100), nullable=False)
    project3_description = db.Column(db.Text, nullable=False)
    project3_skills = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    about_me = db.Column(db.Text, nullable=False)


@app.route('/view-portfolio/<int:id>')
def index(id):
    user_data = UserDetails.query.get(id)
    user = {
            "name": user_data.name,
            "title": user_data.title,
            "profile_picture": user_data.profile_picture,

            "program_name_1": user_data.program_name_1,
            "program_1_university": user_data.program_1_university,
            "program1_year": user_data.program1_year,
            "program1_skills": user_data.program1_skills,

            "program_name_2": user_data.program_name_2,
            "program_2_university": user_data.program_2_university,
            "program2_year": user_data.program2_year,
            "program2_skills": user_data.program2_skills,


            "project1_name": user_data.project1_name,
            "project1_description": user_data.project1_description,
            "project1_skills": [skill.strip() for skill in user_data.project1_skills.split(",")],


            "project2_name": user_data.project2_name,
            "project2_description": user_data.project2_description,
            "project2_skills": [skill.strip() for skill in user_data.project2_skills.split(",")],


            "project3_name": user_data.project3_name,
            "project3_description": user_data.project3_description,
            "project3_skills": [skill.strip() for skill in user_data.project3_skills.split(",")],


            "email": user_data.email,
            "location": user_data.location,
            "phone": user_data.phone,
            "about_me": user_data.about_me
        }



    return render_template("portfolio.html",user=user)



@app.route('/contact-form', methods=['GET','POST'])

def submit_from():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(new_contact)
        db.session.commit()


        return "thank you we will get back to you soon"
    return "yes the form is submited"




@app.route('/list-all-contacts', methods=["GET"])

def list_all_contacts():
    contacts_list = Contact.query.all()
    print("the contacts in our database are - >",contacts_list)
    print("total contacts in our databse is ", len(contacts_list))
    return render_template("list-contacts.html", contacts_list= contacts_list)




@app.route('/create-portfolio', methods=['GET', 'POST'])
def create_portfolio():

    data = {
        'name': '',
        'title': '',
        'profile_picture': '',
        'program_name_1': '',
        'program_1_university': '',
        'program1_year': '',
        'program1_skills': '',
        'program_name_2': '',
        'program_2_university': '',
        'program2_year': '',
        'program2_skills': '',
        'project1_name': '',
        'project1_description': '',
        'project1_skills': '',
        'project2_name': '',
        'project2_description': '',
        'project2_skills': '',
        'project3_name': '',
        'project3_description': '',
        'project3_skills': '',
        'email': '',
        'location': '',
        'phone': '',
        'about_me': ''
    }

    if request.method == 'POST':
        new_portfolio = UserDetails(
            name=request.form['name'],
            title=request.form['title'],
            profile_picture=request.form['profile_picture'],
            program_name_1=request.form['program_name_1'],
            program_1_university=request.form['program_1_university'],
            program1_year=request.form['program1_year'],
            program1_skills=request.form['program1_skills'],
            program_name_2=request.form['program_name_2'],
            program_2_university=request.form['program_2_university'],
            program2_year=request.form['program2_year'],
            program2_skills=request.form['program2_skills'],
            project1_name=request.form['project1_name'],
            project1_description=request.form['project1_description'],
            project1_skills=request.form['project1_skills'],
            project2_name=request.form['project2_name'],
            project2_description=request.form['project2_description'],
            project2_skills=request.form['project2_skills'],
            project3_name=request.form['project3_name'],
            project3_description=request.form['project3_description'],
            project3_skills=request.form['project3_skills'],
            email=request.form['email'],
            location=request.form['location'],
            phone=request.form['phone'],
            about_me=request.form['about_me']
        )

        data = {
            'name': new_portfolio.name,
            'title': new_portfolio.title,
            'profile_picture': new_portfolio.profile_picture,
            'program_name_1': new_portfolio.program_name_1,
            'program_1_university': new_portfolio.program_1_university,
            'program1_year': new_portfolio.program1_year,
            'program1_skills': new_portfolio.program1_skills,
            'program_name_2': new_portfolio.program_name_2,
            'program_2_university': new_portfolio.program_2_university,
            'program2_year': new_portfolio.program2_year,
            'program2_skills': new_portfolio.program2_skills,
            'project1_name': new_portfolio.project1_name,   
            'project1_description': new_portfolio.project1_description,
            'project1_skills': new_portfolio.project1_skills,
            'project2_name': new_portfolio.project2_name,
            'project2_description': new_portfolio.project2_description,
            'project2_skills': new_portfolio.project2_skills,
            'project3_name': new_portfolio.project3_name,
            'project3_description': new_portfolio.project3_description,
            'project3_skills': new_portfolio.project3_skills,
            'email': new_portfolio.email,
            'location': new_portfolio.location,
            'phone': new_portfolio.phone,
            'about_me': new_portfolio.about_me

        }

        if request.form['about_me'] == "generating...":
            if data['email'].strip() == '':
                data['about_me'] = ''
            else:
                data['about_me'] = call_google_ai_model(data)


        else:
            # Add to database and commit
            db.session.add(new_portfolio)
            db.session.commit()
            
            # Get the ID of the newly created portfolio
            portfolio_id = new_portfolio.id
            
            # Create success message with link
            success_message = f"""
            <div style="text-align: center; padding: 50px; font-family: Arial, sans-serif;">
                <h2 style="color: #28a745;">Portfolio Created Successfully!</h2>
                <p style="font-size: 18px; margin: 20px 0;">Your portfolio has been created and is ready to view.</p>
                <div style="margin: 30px 0;">
                    <a href="/view-portfolio/{portfolio_id}" 
                    style="background-color: #007bff; color: white; padding: 12px 30px; 
                            text-decoration: none; border-radius: 5px; font-size: 16px; 
                            display: inline-block; margin: 0 10px;">
                        View Your Portfolio
                    </a>
                </div>
            </div>
            """
            return success_message
            
    return render_template("form2.html", data=data)




@app.route('/all-portfolio', methods=['GET'])

def view_all_portfolio():
    data = UserDetails.query.all()
    return render_template("all-portfolio.html",data=data)




@app.route('/', methods=["GET"])

def landing_page():
    return render_template("landing_page.html")





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)