sentence = input()

new_sentence = sentence.lower()
removed_commas = new_sentence.replace(",", "")
removed_fullstops = removed_commas.replace(".", "")
removed_exclamations = removed_fullstops.replace("!", "")
removed_question_marks = removed_exclamations.replace("?", "")

print(removed_question_marks)