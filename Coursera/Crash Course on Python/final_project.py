# Here are all the installs and imports you will need for your word cloud script and uploader widget

# !pip install wordcloud
# !pip install fileupload
# !pip install ipywidgets
# !jupyter nbextension install --py --user fileupload
# !jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget


def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

file_contents = '''He looked at the graveyard. It was cold and empty. All of the stones had been ripped up and piled like so many flat bricks, one atop another, in the far corner by the wrought iron fence. This had been going on for two endless weeks. In his deep secret coffin he had heard the heartless, wild stirring as the men jabbed the earth with cold spades and tore out the coffins and carried away the withered ancient bodies to be burned. Twisting with fear in his coffin, he had waited for them to come to him.

Today they had arrived at his coffin. But—late. They had dug down to within an inch of the lid. Five o'clock bell, time for quitting. Home to supper. The workers had gone off. Tomorrow they would finish the job, they said, shrugging into their coats.

Silence had come to the emptied tombyard.

Carefully, quietly, with a soft rattling of sod, the coffin lid had lifted.

William Lantry stood trembling now, in the last cemetery on Earth.

"Remember?" he asked himself, looking at the raw earth. "Remember those stories of the last man on earth? Those stories of men wandering in ruins, alone? Well, you, William Lantry, are a switch on the old story. Do you know that? You are the last dead man in the whole damned world!"

There were no more dead people. Nowhere in any land was there a dead person. Impossible? Lantry did not smile at this. No, not impossible at all in this foolish sterile, unimaginative, antiseptic age of cleansings and scientific methods! People died, oh my god, yes. But—dead people? Corpses? They didn't exist!

What happened to dead people?

The graveyard was on a hill. William Lantry walked through the dark burning night until he reached the edge of the graveyard and looked down upon the new town of Salem. It was all illumination, all color. Rocket ships cut fire above it, crossing the sky to all the far ports of earth.

In his grave the new violence of this future world had driven down and seeped into William Lantry. He had been bathed in it for years. He knew all about it, with a hating dead man's knowledge of such things.

Most important of all, he knew what these fools did with dead men.

He lifted his eyes. In the center of the town a massive stone finger pointed at the stars. It was three hundred feet high and fifty feet across. There was a wide entrance and a drive in front of it.

In the town, theoretically, thought William Lantry, say you have a dying man. In a moment he will be dead. What happens? No sooner is his pulse cold when a certificate is flourished, made out, his relatives pack him into a car-beetle and drive him swiftly to—

The Incinerator!

That functional finger, that Pillar of Fire pointing at the stars. Incinerator. A functional, terrible name. But truth is truth in this future world.

Like a stick of kindling your Mr. Dead Man is shot into the furnace.

Flume!

William Lantry looked at the top of the gigantic pistol shoving at the stars. A small pennant of smoke issued from the top.

There's where your dead people go.

"Take care of yourself, William Lantry," he murmured. "You're the last one, the rare item, the last dead man. All the other graveyards of earth have been blasted up. This is the last graveyard and you're the last dead man from the centuries. These people don't believe in having dead people about, much less walking dead people. Everything that can't be used goes up like a matchstick. Superstitions right along with it!"

He looked at the town. All right, he thought, quietly. I hate you. You hate me, or you would if you knew I existed. You don't believe in such things as vampires or ghosts. Labels without referents, you cry! You snort. All right, snort! Frankly, I don't believe in you, either! I don't like you! You and your Incinerators.

He trembled. How very close it had been. Day after day they had hauled out the other dead ones, burned them like so much kindling. An edict had been broadcast around the world. He had heard the digging men talk as they worked!

"I guess it's a good idea, this cleaning up the graveyards," said one of the men.

"Guess so," said another. "Grisly custom. Can you imagine? Being buried, I mean! Unhealthy! All them germs!"

"Sort of a shame. Romantic, kind of. I mean, leaving just this one graveyard untouched all these centuries. The other graveyards were cleaned out, what year was it, Jim?"

"About 2260, I think. Yeah, that was it, 2260, almost a hundred years ago. But some Salem Committee they got on their high horse and they said, 'Look here, let's have just ONE graveyard left, to remind us of the customs of the barbarians.' And the gover'ment scratched its head, thunk it over, and said, 'Okay. Salem it is. But all other graveyards go, you understand, all!'"

"And away they went," said Jim.

"Sure, they sucked out 'em with fire and steam shovels and rocket-cleaners. If they knew a man was buried in a cow-pasture, they fixed him! Evacuated them, they did. Sort of cruel, I say."

"I hate to sound old-fashioned, but still there were a lot of tourists came here every year, just to see what a real graveyard was like."

"Right. We had nearly a million people in the last three years visiting. A good revenue. But—a government order is an order. The government says no more morbidity, so flush her out we do! Here we go. Hand me that spade, Bill.'''

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    new_file = ""
    
    file_content = file_contents.lower()
    
    for charas in file_content:
        if charas.isalpha():
            new_file += charas
        elif charas == " ":
            new_file += ' '
    
    words = new_file.split()
    filtered = []
    
    for x in words:
        for y in uninteresting_words:
            if x in y:
                x = x.replace(y, '')
        filtered.append(x)
    listed_filtered = [element for element in filtered if element.strip()]
          
    dict_file = {}
    for ind in listed_filtered:
        if ind not in dict_file:
            dict_file[ind] = 0
        dict_file[ind] += 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict_file)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
