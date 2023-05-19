from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from gameplay_rental.forms import GameForm
from gameplay_rental.models import Game, db

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    print("YO")
    return render_template('index.html')


@site.route('/profile')
@login_required
def profile():
    # my_game = GameForm()

    # try:
    #     if request.method == 'POST' and my_game.validate_on_submit():
    #         search = my_game.search.data
    #         search_precise = my_game.search_precise.data
    #         search_exact = my_game.search_exact.data
    #         platforms = my_game.platforms.data
    #         stores = my_game.stores.data
    #         developers = my_game.developers.data
    #         dates = my_game.dates.data
    #         publishers = my_game.publishers.data
            
    #         game = Game(search = search, search_precise = search_precise, search_exact = search_exact, platforms = platforms, stores = stores, developers = developers, dates = dates, publishers = publishers)
            
    #         db.session.add(game)
    #         db.session.commit()

    #         return redirect(url_for('site.home'))
    
    # except:
    #     raise Exception('Invalid Form Data: Please Check Your Form')
    return render_template('profile.html')
    



# logged_user = User.query.filter(User.token == user_token).first()

#             if logged_user:
#                 db.session.add(character)
#                 db.session.commit()
#                 print(f"The character have successfully added {character.name} to {logged_user.name}'s Collection!", 'add-success')
#                 return redirect(url_for('site.addcharacter'))
#             else:
#                 print('Please enter valid token', 'token-failed')
                
#             return redirect(url_for('site.addcharacter'))
#     except:
#         raise Exception('Invalid: Please Check Your Form')

#     return render_template('add.html', form = form)

# @site.route('/site profile')
# @login_required
# def profile():
#     logged_user = User.query.filter(User.token == current_user.token).first()
#     usercollection = Character.query.filter(Character.user_token == logged_user.token).all()
#     return render_template('profile.html', entries = usercollection)





# r = requests.get('https://api.rawg.io/api/games?key=86962d8203ea4e4587007fc6459fcffa')
# print(r)
# games = r.json()['results']
# def search():
#     return render_template('profile.html', games = games)


# <!-- {{ form.hidden_tag() }}
# <div class="search-box">
# <fieldset id="password-field">
#     {{ form.game.label }}
#     {{ form.game(class = "form-control", placeholder = "Enter Game Here...", type="search") }}
# </fieldset>
# {{ form.submit_button(class="btn btn-primary btn-black mt-1") }}
# </div> -->