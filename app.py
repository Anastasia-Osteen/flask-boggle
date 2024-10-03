from boggle import Boggle
from flask import Flask, request, render_template, session, redirect, flash

app = Flask(__name__)
boggle = Boggle()


@app.route('/')
def home():
    board = boggle.make_board()
    session['board'] = board
    highscore = session.get('highscore', 0)
    plays = session.get('plays', 0)

    score = scores(highscore)
    play_num = play_number(plays)
    
    return render_template('index.html', board=board, score=score, play_num=play_num)

def scores(score):
    highscore = session.get('highscore', 0)
    session['highscore'] = max(score, highscore)

    return session['highscore']


def play_number(plays):
    plays = session.get('plays', 0)
    session['plays'] = plays + 1

    return session['plays']


@app.route('/valid-word')
def valid_word_check():
    word = request.args['guess']
    board = session['board']
    valid_word = boggle.check_valid_word(board, word)

    flash(f"result: {valid_word}")

    return redirect('/')


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True) 