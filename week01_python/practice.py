
# total_predictions = 80
# # correct_predictions = 60
# correct_predictions = 40
# incorrect_predictions = total_predictions - correct_predictions
# # incorrect_predictions = 20
# accuracy = correct_predictions / total_predictions

# error_rate = incorrect_predictions / total_predictions * 100

# # print ("incorrect_predictions:",incorrect_predictions / total_predictions * 100)
# # print (incorrect_predictions)
# print(error_rate)

# if error_rate <= 5:
#     print ("it is within the target")

# elif error_rate > 5 and error_rate <=  10: 
#     print ("Meets the target")
# else: 
#     print ("It is above the target")


# LIST
accuracies = [0.15, 0.45, 0.95, 0.45]

# print(len(accuracies))

# accuracies.append(0.66)
# accuracies[2] = 0.77
# print(accuracies)
# print(accuracies[0])
# print(accuracies[3])
# accuracies.append(0.11)
# accuracies[1]=0.11
# print(accuracies)



# LOOP[]
# for accuracy in accuracies:
#  if accuracy >= 0.95:
#     print(accuracy)
#  else:
#     print("none")

# accuracies = [0.75, 0.96, 0.91, 0.98, 0.95]
# count = 0
# for accuracy in accuracies:
#  if accuracy >= 0.90:
#     count +=1
# print(count)

labels = [" Positive ", "NEGATIVE", " positive", "Negative  "]

# for label in labels:
#     clean_label = label.strip().lower()
#     print(clean_label)

count = 0 
for label in labels:
    clean_label = label.strip().lower()

    if clean_label == "positive":
        count +1
print(count)
