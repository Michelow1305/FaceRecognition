import matplotlib.pyplot as plt
import seaborn as sns


def plot_face_data(data):
    # Extract relevant data from the JSON
    race = data[0]['race']
    gender = data[0]['gender']
    emotions = data[0]['emotion']

    # Create subplots for emotions, gender, and race
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Plot the emotions
    axes[0].set_title('Emotions')
    sns.barplot(x=list(emotions.keys()), y=list(emotions.values()), ax=axes[0])
    axes[0].set_ylabel('Probability')

    # Plot the gender distribution
    axes[1].set_title('Gender Distribution')
    labels_gender = list(gender.keys())
    sizes_gender = list(gender.values())
    axes[1].pie(sizes_gender, labels=labels_gender, autopct='%1.1f%%', startangle=140)

    # Plot the race distribution
    axes[2].set_title('Race Distribution')
    labels_race = list(race.keys())
    sizes_race = list(race.values())
    axes[2].pie(sizes_race, labels=labels_race, autopct='%1.1f%%', startangle=140)

    plt.tight_layout()

    # Show the plot
    plt.show()


def printDominantValues(data):
    # Extract relevant data from the JSON
    dominant_emotion = data[0]['dominant_emotion']
    dominant_gender = data[0]['dominant_gender']
    dominant_race = data[0]['dominant_race']
    age = data[0]['age']

    # Print the extracted information
    print(f"Dominant Emotion: {dominant_emotion}")
    print(f"Dominant Gender: {dominant_gender}")
    print(f"Dominant Race: {dominant_race}")
    print(f"Age: {age} years")
