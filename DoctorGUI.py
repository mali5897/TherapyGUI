from breezypythongui import EasyFrame
import random


class DoctorGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Therapy session", width=360, height=300, resizable=True)
        
        # Add label for the conversation display
        self.label = self.addLabel(text="Good morning, I hope you are well today.\nWhat can I do for you?", 
                                   row=0, column=0, sticky="NEWS", rowspan=2)
        
        # Add a text area to display conversation (initially blank)
        self.responseArea = self.addTextArea("", row=2, column=0, width=30, height=5)
        
        # Add a text field to type the patient's message
        self.inputField = self.addTextField("", row=3, column=0, width=25)
        
        # Add a button to send the patient's input
        self.sendButton = self.addButton(text="Send", row=3, column=1, command=self.handleResponse)
        
    def handleResponse(self):
        """Handle the interaction with the patient and provide a reply."""
        user_input = self.inputField.getText()  # Get the input from the text field
        
        if user_input.upper() == "QUIT":
            self.close()  # Exit the GUI if "QUIT" is entered
        
        # Generate the reply using the reply function
        doctor_reply = self.reply(user_input)
        
        # Update the response area with both the patient's input and the doctor's reply
        current_text = self.responseArea.getText()
        new_text = current_text + "\nPatient: " + user_input + "\nDoctor: " + doctor_reply
        self.responseArea.setText(new_text)
        
        # Clear the input field for the next message
        self.inputField.setText("")
        
    def reply(self, sentence):
        """Generate a reply to the sentence."""
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(self.hedges)
        else:
            return random.choice(self.qualifiers) + self.changePerson(sentence)
        
    def changePerson(self, sentence):
        """Replace first person pronouns with second person pronouns."""
        words = sentence.split()
        replyWords = []
        replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours"}
        
        for word in words:
            replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)

    # Define hedges and qualifiers as part of the class
    hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")
    qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")


def main():
    DoctorGUI().mainloop()


if __name__ == "__main__":
    main()
