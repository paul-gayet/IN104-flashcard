import tkinter as tk
import datetime
import pickle
import random
from classe_for_flashcard import Card, Deck

"""
We intialise a deck
"""
mydeck=Deck()

class Window(tk.Frame):
	"""
	Class for the master widget
	"""
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title(' ')
		self.master.config(background='#40E0D0')
		self.master.geometry("800x600")
		self.master.minsize(500,400)
		self.pack(fill=tk.BOTH, expand=0)

		welcome = tk.Label(self.master, text="Welcome to your training",font=("Helvetica",50),bg='#40E0D0',fg='white').pack(expand=tk.YES)
		
		load_file = tk.Button(self.master,text="Load a file",bg='white',fg='#40E0D0',command=self.choose_file_to_game).pack(expand=tk.YES)

		edit_flashcards = tk.Button(self.master,text="Edit flashcards ",bg='white',fg='#40E0D0',command=self.manage).pack(expand=tk.YES)
		leave = tk.Button(self.master,text="Quit",bg='white',fg='#40E0D0',command=self.quit).pack(expand=tk.YES)





#Quit the game

	def quit(self):
		exit()


#To come back to the welcome page

	def retour(self):
		for widget in root.winfo_children():
			widget.destroy()
		tk.Frame.__init__(self, master=None)
		self.init_window()



#Main fonction of the management system, where one's can decide to add/edit/delete cards or save/load a file


	def manage(self) :
		for widget in root.winfo_children():
			widget.destroy()
		information = tk.Label(self.master,text='You have ' + str(len(mydeck.deck)) + ' cards in your deck',fg='white',bg='#40E0D0').pack(expand=tk.YES)

		add_button=tk.Button(self.master, text='Add a flashCard',bg='white',fg='#40E0D0',command=self.add_card).pack(expand=tk.YES) #line 81
		edit_button=tk.Button(self.master, text='Edit a flashCard',bg='white',fg='#40E0D0',command=self.choose_card_to_edit).pack(expand=tk.YES)#line134

		delete_button=tk.Button(self.master, text='Delete a flashCard',bg='white',fg='#40E0D0',command=self.choose_card_to_delete).pack(expand=tk.YES)#line 310

		save_button=tk.Button(self.master, text='Save a deck',bg='white',fg='#40E0D0',command=self.choose_name_file_to_save).pack(expand=tk.YES)#line358

		load_button=tk.Button(self.master, text='Load a deck',bg='white',fg='#40E0D0',command=self.choose_file_to_load).pack(expand=tk.YES)#line392

		load_csv_button=tk.Button(self.master, text='Load a deck from a csv file', bg='white', fg='#40E0D0',command=self.choose_file_csv).pack(expand=tk.YES) #line423
	
		return_button=tk.Button(self.master,text='Return',bg='white',fg='#40E0D0',command=self.retour).pack(expand=tk.YES)# line 48
		

#fonctions to add a card in a deck

	def add_card(self):
		for widget in root.winfo_children():
			widget.destroy()
		global entry_title,entry_question,entry_answer,entry_subject
	
	#user enter all informations to create a card"
	
		instruction_for_title = tk.Label(self.master,text="What is the title",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_title = tk.Entry(self.master)
		entry_title.focus_set()
		entry_title.pack(expand=tk.YES)

		instruction_for_question = tk.Label(self.master,text=" What is the question",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_question=tk.Entry(self.master)
		entry_question.focus_set()
		entry_question.pack(expand=tk.YES)

		instruction_for_answer = tk.Label(self.master,text="What is the answer",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_answer=tk.Entry(self.master)
		entry_answer.focus_set()
		entry_answer.pack(expand=tk.YES)

		instruction_for_subject=tk.Label(self.master,text="What is the subject",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_subject=tk.Entry(self.master)
		entry_subject.focus_set()
		entry_subject.pack(expand=tk.YES)

		back=tk.Button(self.master,text='Return',bg='white',fg='#40E0D0',command=self.manage).pack(side=tk.LEFT,pady=25) #line 59
		valid=tk.Button(self.master,text="Valid",fg='#40E0D0',bg='white',command=self.create_card).pack(side=tk.RIGHT,pady=25) #line114


#save the entries and call classe_for_flashcard

	def create_card(self) :
		global entry_title,entry_question,entry_answer,entry_subject
		title=str(entry_title.get())
		question=str(entry_question.get())
		answer=str(entry_answer.get())
		subject=str(entry_subject.get())
		
		#fonction in classe_for_flashcard
		
		mydeck.add_card(title,question,answer,subject) 
		self.manage()
		



#fonctions to edit a card

	
	#fonction to choose which card to edit
	
	def choose_card_to_edit (self): 
		for widget in root.winfo_children():
			widget.destroy()
		global entry_card_to_edit
		instruction=tk.Label(self.master,text="What is the title of the card that you want to edit?",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		
		entry_card_to_edit=tk.Entry(self.master)
		entry_card_to_edit.focus_set()
		entry_card_to_edit.pack(expand=tk.YES)

		Valid=tk.Button(self.master,text="Valid",fg='#40E0D0',bg='white',command=self.choose_what_to_edit).pack(side=tk.RIGHT,pady=25)
		Back=tk.Button(self.master,text='Back',bg='white',fg='#40E0D0',command=self.manage).pack(side=tk.LEFT,pady=25) #line 59

	
	#fonction to choose what to edit : title/question/asnwer/subject
	
	def choose_what_to_edit (self):
		global entry_card_to_edit,card
		title=str(entry_card_to_edit.get())
		card=mydeck.search_card(title)
		if card==None :
			
			#Test if the card is in the deck
			
			self.top_level3=tk.Toplevel(root)
			self.top_level3.geometry("480x380")
			self.top_level3.config(background='#40E0D0')
			self.top_level3.title("Erreur")
			information=tk.Label(self.top_level3,text="The card doesn't exist, please try an other",fg='#40E0D0',bg='white').pack(expand=tk.YES)
			back=tk.Button(self.top_level3,text="return",bg='#40E0D0',fg='white',command=self.choose_card_to_edit).pack(side=tk.RIGHT,pady=25)

		else :
			for widget in root.winfo_children():
				widget.destroy()

			instruction_to_edit=tk.Label(self.master,text="What would you like to edit?",fg='#40E0D0',bg='white').pack(expand=tk.YES)

			edit_title_button=tk.Button(self.master,text="The title?",bg='white',fg='#40E0D0',command=self.edit_title).pack(expand=tk.YES,pady=25)#line 187

			edit_question_button=tk.Button(self.master,text="The Question",bg='white',fg='#40E0D0',command=self.edit_question).pack(expand=tk.YES,pady=25)#line 217

			edit_answer_button=tk.Button(self.master,text="The answer?",bg='white',fg='#40E0D0',command=self.edit_answer).pack(expand=tk.YES,pady=25)#line 247

			edit_subject_button=tk.Button(self.master,text="The subject?",bg='white',fg='#40E0D0',command=self.edit_subject).pack(expand=tk.YES,pady=25)#line 277

			Back=tk.Button(self.master,text="Back",fg='#40E0D0',bg='white',command=self.manage).pack(side=tk.LEFT,pady=25)#line59
			


	
	#fonction to edit the title
			

	def edit_title(self):
		for widget in root.winfo_children():
			widget.destroy()
		global card,entry_edit_title
		instruction=tk.Label(self.master,text="What is the new title",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_edit_title=tk.Entry(self.master) #user enter the new title
		entry_edit_title.focus_set()
		entry_edit_title.pack(expand=tk.YES)
		Valid=tk.Button(self.master,text="Valid",bg='white',fg='#40E0D0',command=self.record_edit_title).pack(expand=tk.YES,pady=25) #line201

	
	#fonction to save the new title, then send us to the management window
	
	
	def record_edit_title(self) :
		global entry_edit_title,card
		new_title=str(entry_edit_title.get())
		card.edit_title(new_title)	#call classe_for_flashcard
		self.top_level3=tk.Toplevel(root)
		self.top_level3.geometry("480x380")
		self.top_level3.config(background='#40E0D0')
		self.top_level3.title("")
		information=tk.Label(self.top_level3,text="The new title is : " +card.title ,fg='white',bg='#40E0D0').pack(expand=tk.YES)
		back=tk.Button(self.top_level3,text="Return",bg='white',fg='#40E0D0',command=self.manage).pack(side=tk.RIGHT,pady=25)########ligne 59


		
	#fonction to edit the question 
		

	def edit_question(self):
		for widget in root.winfo_children():
			widget.destroy()
		global card,entry_edit_question
		instruction=tk.Label(self.master,text="What is the new question :",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_edit_question=tk.Entry(self.master) #user enter the new question
		entry_edit_question.focus_set()
		entry_edit_question.pack(expand=tk.YES)
		Valid=tk.Button(self.master,text="Valid",bg='white',fg='#40E0D0',command=self.record_edit_question).pack(expand=tk.YES,pady=25) #line 231

	
	#fonction to save the new question

	
	def record_edit_question (self) :
		global entry_edit_question,card
		new_question=str(entry_edit_question.get())
		card.edit_question(new_question) #call classe_for_flashcard
		self.top_level3=tk.Toplevel(root)
		self.top_level3.geometry("480x380")
		self.top_level3.config(background='#40E0D0')
		self.top_level3.title("")
		information=tk.Label(self.top_level3,text="The new question is : " +card.question,fg='white',bg='#40E0D0').pack(expand=tk.YES)
		Back=tk.Button(self.top_level3,text="Return",fg='#40E0D0',bg='white',command=self.manage).pack(side=tk.RIGHT,pady=25) #ligne 59


	
	#fonction to edit the answer


	def edit_answer(self):
		for widget in root.winfo_children():
			widget.destroy()
		global card,entry_edit_answer
		instruction=tk.Label(self.master,text="What is the new answer ? ",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_edit_answer=tk.Entry(self.master) #user enter the new answer
		entry_edit_answer.focus_set()
		entry_edit_answer.pack(expand=tk.YES)
		Valid=tk.Button(self.master,text="Valid",bg='white',fg='#40E0D0',command=self.record_edit_answer).pack(expand=tk.YES,pady=25) #line261
	
	
	#fonction to save the new answer
	

	def record_edit_answer(self) :
		global entry_edit_answer,card
		new_answer=str(entry_edit_answer.get())
		card.edit_answer(new_answer) #call classe_for_flashcard
		self.top_level3=tk.Toplevel(root)
		self.top_level3.geometry("480x380")
		self.top_level3.config(background='#40E0D0')
		self.top_level3.title("")
		information=tk.Label(self.top_level3,text="The new answer is : " +card.answer,fg='white',bg='#40E0D0').pack(expand=tk.YES)
		Back=tk.Button(self.top_level3,text="Return",bg='white',fg='#40E0D0',command=self.manage).pack(side=tk.RIGHT,pady=25)#ligne 59


	
	#fonction to edit subject
	

	def edit_subject(self):
		for widget in root.winfo_children():
			widget.destroy()
		global card,entry_edit_subject
		instruction=tk.Label(self.master,text="What is the new subject ?",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_edit_subject=tk.Entry(self.master) #user enter the new subject
		entry_edit_subject.focus_set()
		entry_edit_subject.pack(expand=tk.YES)
		Valid=tk.Button(self.master,text="Valid",bg='white',fg='#40E0D0',command=self.record_edit_subject).pack(expand=tk.YES,pady=25)#line291

	
	#fonction to save the new subject
	
	
	def record_edit_subject(self) :
		global entry_edit_subject,card
		new_subject=str(entry_edit_subject.get())
		card.edit_subject(new_subject)	#call classe_for_flashcard
		self.top_level3=tk.Toplevel(root)
		self.top_level3.geometry("480x380")
		self.top_level3.config(background='#40E0D0')
		self.top_level3.title("")
		information=tk.Label(self.top_level3,text="The new subject is : " +card.subject,fg='white',bg='#40E0D0').pack(expand=tk.YES)
		Back=tk.Button(self.top_level3,text="Return",fg='#40E0D0',bg='white',command=self.manage).pack(side=tk.RIGHT,pady=25)#line 59


#fonctions to delete a card


	
	#fonction to choose the carte to delete
	

	def choose_card_to_delete(self): 
		for widget in root.winfo_children():
		 	widget.destroy()
		global entry_card_to_delete
		instructiontruction=tk.Label(self.master,text="Which card do you want to delete ?",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_card_to_delete=tk.Entry(self.master) #user enter the title of the card to delete
		entry_card_to_delete.focus_set()
		entry_card_to_delete.pack(expand=tk.YES)
		Valid=tk.Button(self.master,text="Valid",fg='#40E0D0',bg='white',command=self.delete).pack(side=tk.RIGHT,pady=25)########ligne 290
		Back=tk.Button(self.master,text='Return',fg='#40E0D0',bg='white',command=self.manage).pack(side=tk.LEFT,pady=25)########ligne 59



	
	#fonction to delete a card
	

	def delete(self):
		global entry_card_to_delete,card
		title=str(entry_card_to_delete.get())
		card=mydeck.search_card(title) #call classe_for_flashcard
		if card==None :
			
			#Test if the card is in the deck, otherwise return to the fonction choose_card_to_delete
			
			self.top_level3=tk.Toplevel(root)
			self.top_level3.geometry("420x380")
			self.top_level3.config(background='#40E0D0')
			self.top_level3.title("Erreur")
			information=tk.Label(self.top_level3,text="There is no card with that title, please try again",fg='white',bg='#40E0D0').pack(expand=tk.YES)
			Back=tk.Button(self.top_level3,text="Return",bg='white',fg='#40E0D0',command=self.choose_card_to_delete).pack(side=tk.RIGHT,pady=25)#line 310
	
		else :
			for widget in root.winfo_children():
				widget.destroy()
			mydeck.delete_card(card) #call classe_for_flashcard
			information=tk.Label(self.master,text="The card has been delated successfully",fg='white',bg='#40E0D0').pack(expand=tk.YES)
			back=tk.Button(self.master,text="Return",fg='#40E0D0',bg='white',command=self.manage).pack(side=tk.RIGHT,pady=25) #line59



#fonction to save the deck

	
	
	#fonction to choose the file to save
	

	def choose_name_file_to_save(self): 
		for widget in root.winfo_children():
			widget.destroy()
		global entry_name_file
		instruction=tk.Label(self.master,text="Enter the name of the file but it must be .pickle)",fg='white',bg='#40E0D0').pack(expand=tk.YES) #
		entry_name_file=tk.Entry(self.master) #user enter the name of the file to save
		entry_name_file.focus_set()
		entry_name_file.pack(expand=tk.YES)
		valid=tk.Button(self.master,text="Valid",fg='#40E0D0',bg='white',command=self.save_file).pack(side=tk.RIGHT,pady=25)#line 373
		back=tk.Button(self.master,text='Return',fg='#40E0D0',bg='white',command=self.manage).pack(side=tk.LEFT,pady=25)#line 59

	
	#fonction to save the file
	

	def save_file(self):
		global entry_name_file
		name_file=str(entry_name_file.get())
		mydeck.save_deck(name_file) #call classe_for_flashcard
		for widget in root.winfo_children():
			widget.destroy()
		information=tk.Label(self.master,text="The file has been save successfully",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		back=tk.Button(self.master,text="Return",fg='white',bg='#40E0D0',command=self.manage).pack(side=tk.RIGHT,pady=25) #line59




#fonction to load a deck

	
	
	#fonction to choose the file to load
	

	def choose_file_to_load(self):
		for widget in root.winfo_children():
			widget.destroy()
		global entry_file_to_load
		information=tk.Label(self.master,text="Which file do you want to load ?",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_file_to_load=tk.Entry(self.master) #user enter the name of the file to load
		entry_file_to_load.focus_set()
		entry_file_to_load.pack(expand=tk.YES)
		Valid=tk.Button(self.master,text="Valid",bg='white',fg='#40E0D0',command=self.load_file).pack(side=tk.RIGHT,pady=25)#line408
		back=tk.Button(self.master,text='Return',fg='#40E0D0',bg='white',command=self.manage).pack(side=tk.LEFT,pady=25)#line59

	
	#fonction to load the file



	def load_file(self):
		global entry_file_to_load
		name_file=str(entry_file_to_load.get())
		mydeck.load_deck(name_file) #call classe_for_flashcard
		for widget in root.winfo_children():
			widget.destroy()
		information=tk.Label(self.master,text="Your file has been successfully loaded",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		back=tk.Button(self.master,text="",fg='white',bg='#40E0D0',command=self.manage).pack(side=tk.RIGHT,pady=25)#line 59

	

	
	#same fonctions but for a csv.file

	def choose_file_csv(self):
		for widget in root.winfo_children():
			widget.destroy()
		global entry_file_to_load_csv
		information=tk.Label(self.master,text="Which file.csv do you want to load ?",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		entry_file_to_load_csv=tk.Entry(self.master)
		entry_file_to_load_csv.focus_set()
		entry_file_to_load_csv.pack(expand=tk.YES)
		Valid=tk.Button(self.master,text="Valid",bg='white',fg='#40E0D0',command=self.load_file_csv).pack(side=tk.RIGHT,pady=25)#line 436
		back=tk.Button(self.master,text='Return',fg='#40E0D0',bg='white',command=self.manage).pack(side=tk.LEFT,pady=25)#line59



	def load_file_csv(self):
		global entry_file_to_load_csv
		name_file=str(entry_file_to_load_csv.get())
		mydeck.load_deck_from_csv(name_file)
		for widget in root.winfo_children():
			widget.destroy()
		information=tk.Label(self.master,text="Your file has been loaded successfully",fg='white',bg='#40E0D0').pack(expand=tk.YES)
		back=tk.Button(self.master,text="Return",bg='white',fg='#40E0D0',command=self.manage).pack(expand=tk.YES) #line59





#The training system


	
	
	#fonction to choose the file to load and start the session


	def choose_file_to_game(self):
		today = datetime.datetime.now()
		self.top_level=tk.Toplevel(root)
		self.top_level.geometry("380x240")
		self.top_level.config(background='#40E0D0')
		self.top_level.title('Load a file.pickle')
		self.pack(fill=tk.BOTH, expand=1)
		global entry_file_to_game
		entry_file_to_game=tk.Entry(self.top_level,text="File's name?",font=("Helvetica",12)) #user enter the name of the file
		entry_file_to_game.focus_set() 
		entry_file_to_game.pack(side=tk.LEFT,pady=25)
		Valid=tk.Button(self.top_level,text="Valid",bg='white',fg='#40E0D0',command=self.load_file_to_game).pack(side=tk.RIGHT,pady=25)#line 477
	
	
	
	#fonction to load the file and sort which card to review during the ssession
	


	def load_file_to_game(self):
		global entry_file_to_game, file_to_save
		name_file_to_game=str(entry_file_to_game.get())
		file_to_save = name_file_to_game
		try:
			mydeck.load_deck(name_file_to_game) #call classe_for_flashcard
			for widget in root.winfo_children():
				if isinstance(widget,tk.Toplevel):
					widget.destroy()
			self.top_level3=tk.Toplevel(root)
			self.top_level3.geometry("320x280")
			self.top_level3.config(background='#40E0D0')
			self.top_level3.title("")
			information=tk.Label(self.top_level3,text="File loaded",fg='white',bg='#40E0D0').pack(expand=tk.YES)

			global today
			global delay
			global need_to_be_reviewed 
			today= datetime.datetime.now()
			one_day = datetime.timedelta(1,0,0)
			three_day = datetime.timedelta(3,0,0)
			nine_day = datetime.timedelta(9,0,0)
			#each bin for space repetition is represented by an element of the list delay

			delay=[today,one_day,three_day,nine_day]

			
			#check if the difference in date between when the card was last reviewed and the delay is set to a date that is before today
			
			need_to_be_reviewed=[]
			for card in mydeck.deck:
				if card.date+delay[card.location]<today:
					card.reviewed= True
					need_to_be_reviewed.append(card)
			random.shuffle(need_to_be_reviewed)
			continu=tk.Button(self.top_level3,text="Continue",bg='white',fg='#40E0D0',command=self.write_answer).pack(expand=tk.YES) #line528
		
		
		#if there is an error
		
		except IOError : 
			self.top_level2=tk.Toplevel(root)
			self.top_level2.geometry("320x220")
			self.top_level2.config(background='#40E0D0')
			self.top_level2.title("Error")
			information_error=tk.Label(self.top_level2,text="That file doesn't exist",fg='white',bg='#40E0D0').pack(expand=tk.YES)

	
	#fonction to show the question and write the answer
	



	def write_answer(self):
		global need_to_be_reviewed
		for widget in root.winfo_children():
				widget.destroy()
		self.master.geometry("680x480")

		if need_to_be_reviewed == []: 
			
			#when all the card have been reviewed, the session is finished
			
			information=tk.Message(self.master,text="End of the training for today, come back tomorrow",font=("Helvetica",30),bg='#40E0D0',fg='white').pack(expand=tk.YES)
			quit=tk.Button(self.master, text='Quit',bg='white',fg='#40E0D0',command=self.quit).pack(expand=tk.YES)#line 42
			back=tk.Button(self.master,text='Return',fg='#40E0D0',bg='white',command=self.retour).pack(expand=tk.YES)#line 48
		else :
			global card_playing
			global saisie	
			card_playing=need_to_be_reviewed[0]
			global entry_answer
			question=card_playing.question
			label=tk.Label(self.master,text=question,font=("Helvetica",30),bg='#40E0D0',fg='white').pack(expand=tk.YES) #show the question
			entry_answer=tk.Entry(self.master,font=("Helvetica",12)) #user enter his answer
			entry_answer.focus_set()
			entry_answer.pack(side=tk.LEFT,pady=25)
			check_answer=tk.Button(self.master,text="Check your answer",bg='white',fg='#40E0D0',command=self.check_answer).pack(side=tk.RIGHT,pady=25)#line559
			back=tk.Button(self.master,text='Return',fg='#40E0D0',bg='white',command=self.retour).pack(expand=tk.YES) #line42
	
	
	
	#check the answer given and move the card to the right bin (change location)
	
			
	def check_answer(self):
		global card_playing
		global entry_answer
		global delay
		global today
		global need_to_be_reviewed
		global file_to_save
		answer=str(entry_answer.get())
		
		#if the answer is good : congrats and move the card to the next bin
		
		if answer.lower()==card_playing.answer.lower():
			self.top_level=tk.Toplevel(root)
			self.top_level.geometry("520x160")
			self.top_level.config(background='#40E0D0')
			self.top_level.title("Congratulation")
			congrats=tk.Label(self.top_level,text="It's a good answer !! Well done",fg='white',bg='#40E0D0').pack(expand=tk.YES)
			if card_playing.location < len(delay)-1:
				card_playing.location+=1       
			card_playing.date=today
		
		#if the answer is wrong : show the correct one and throw the card in the first bin
		
		else: 
			self.top_level=tk.Toplevel(root)
			self.top_level.geometry("520x160")
			self.top_level.config(background='#40E0D0')
			self.top_level.title("Oh..sorry")
			information=tk.Label(self.top_level,text="Sorry, the correct answer is : " + card_playing.answer,fg='white',bg='#40E0D0').pack(expand=tk.YES)
			card_playing.location=0
			card_playing.date=today
		
		#delete the card from the list to be reviewed
		
		need_to_be_reviewed.pop(0)
		
		#save the deck because card.date et card.location have changed
		
		mydeck.save_deck(file_to_save)
		
		#call write_answer for the next card!
		
		next_card=tk.Button(self.top_level,text='Next question',bg='white',fg='#40E0D0',command=self.write_answer).pack(pady=25) #line528
	
root = tk.Tk()

app = Window(root)
root.mainloop()

