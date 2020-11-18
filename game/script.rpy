﻿        

#    if not persistent.set_volumes:
#        persistent.set_volumes = True
#        _preferences.volumes['music'] *= .40
init python:
    config.overlay_screens.append("keymap_screen")
    if not persistent.set_volumes:
        persistent.set_volumes = True
        try:
            _preferences.volumes['music'] *= .50
        except KeyError:
            _preferences.volumes['music'] = .50        
    
init:
#this changes skip to mousewheel
    $ config.keymap['rollforward'].remove('mousedown_5')
    $ config.keymap['rollback'].remove('mousedown_4')
    $ config.keymap['dismiss'].append('mousedown_5')
    $ config.keymap['rollforward'].append('K_q')
    $ config.keymap['rollback'].append('K_w')
define config.game_menu_music = "gamemenu.ogg"
screen keymap_screen():
    key "K_y" action ShowMenu('history')
# Declare characters used by this game. The color argument colorizes the name of the character.
define t = Character("Twilight Sparkle", color="#800080")
define a = Character(_("[povname]"), color="#228B22")
define z = Character(_("Zecora"), color="#696969")
define l = Character(_("Lyra"), color="#98ff98")
define s = Character(_("Spike"), color="#DA70D6")
define c = Character(_("Celestia"), color="#808080")
define r = Character(_("Rarity"), color="#808080")
define p = Character(_("Pinkie"), color="#FF69B4")
define rd = Character(_("Rainbow Dash"), color="#48D1CC")
define f = Character(_("Fluttershy"), color="#FFFF66")
define aj = Character(_("Applejack"), color="#FFA500")


default povname = "Anonymous"

image chapter = ParameterizedText(xalign=0.5, yalign=0.3)

# The game starts here.

#default a = 2
#label start:
#  $ a = 3
#  if a == 2:
#    e "Do a thing"
#  else:
#    e "Do another thing"

#List of songs: spooky.mp3 (original Everfree song), Pinkiepie.mp3, intro.mp3, mainmenu.ogg, gamemenu.ogg, mysterious.ogg, sleeping.ogg, magical.ogg, exciting.ogg, boardgame.ogg

image zecora standing = im.MatrixColor(
    "zecora stand.png", 
    im.matrix.tint(.44,.65,.75)
    *im.matrix.brightness(-0.07))
    
screen party():
  imagebutton:
    focus_mask "pinkiebutton_idle_img.png"
    idle "pinkiebutton_idle_img.png"
    hover "pinkiebutton_hover_img.png"
    pos (583,27)
    action Jump("pinkieparty")
  imagebutton:
    focus_mask "dashbutton_idle_img.png"
    idle "dashbutton_idle_img.png"
    hover "dashbutton_hover_img.png"
    pos (0,70)
    action Jump("dashparty")
  imagebutton:
    focus_mask "raritybutton_idle_img.png"
    idle "raritybutton_idle_img.png"
    hover "raritybutton_hover_img.png"
    pos (927,369)
    action Jump("rarityparty")
  imagebutton:
    focus_mask "twilightbutton_idle_img.png"
    idle "twilightbutton_idle_img.png"
    hover "twilightbutton_hover_img.png"
    pos (1267,360)
    action Jump("twilightparty")
  imagebutton:
    focus_mask "fluttershybutton_idle_img.png"
    idle "fluttershybutton_idle_img.png"
    hover "fluttershybutton_hover_img.png"
    pos (661,406)
    action Jump("fluttershyparty")
  imagebutton:
    focus_mask "ajbutton_idle_img.png"
    idle "ajbutton_idle_img.png"
    hover "ajbutton_hover_img.png"
    pos (160,405)
    action Jump("applejackparty")
  imagebutton:
    focus_mask "spikebutton_idle_img.png"
    idle "spikebutton_idle_img.png"
    hover "spikebutton_hover_img.png"
    pos (0,538)
    action Jump("spikeparty")
    
   

#Todo list: Add vectors for Celestia and Twilight in and code Lyra behind the table in the diner. 
#Make the rest of Zecora's sprites dark in the forest


label start:

    "Press TAB to fast forward, Y for message history, W to go back once, H to hide the sprites and text box, and mouse wheel, spacebar, or left click to advance the text."
    menu:

        "Where do you want to go?"
        
        "Start":
            jump anon

        "Zecora":
            jump zecora

        "Twilight":
            jump meetingtwilight
            
        "Celestia":
            jump celestia
            
        "Lyra":
            jump lyra

label anon:
    show chapter "DAY 1"
    scene black
    play music "intro.mp3"   
    "Another dead-end night, just the same thing, over and over."
    "Story of my life."
    "I'm on my way to work: an absolutely hellish job."
    scene bg dishwash with dissolve
    play sound "audio/dishwashing.mp3"    
    "The kitchen is gray and steel and everything feels muffled, except for the slamming of dishes and chattering of coworkers."
    "Worse, I'm late, which adds to my stress."
    "The restaurant is heavily frequented and it's very busy, as expected."
    "It's very stressful."
    scene bathroom with dissolve
    stop sound 
    "I manage to find a time when I'm not being assaulted by dishes, and I use that window of time to go the bathroom, bringing my phone with me."
    "The lights are motion-activated and turn off automatically as I sit there on the pot, messing with my phone."
    "I'm used to it, though."
    "You know what they say: boss makes a dollar, I make a dime, and that's why I poop on company time."
    "Bored and depressed, I click the new 4chan board /mlp/ to see what it was about."
    "I mispress the ad with my thumb trying to scroll down."
    "A window opens up on my phone's browser."
    a "Damn..."
    "Suddenly, everything flashes."
    "I realize that after a while in the darkness, I can't really feel anything or see much beyond the available light the phone gives off."
    "I attempt to reach out to find a wall with no success."
    "Okay, I'm really panicking now!"
    "I'm freaking out and a bead of sweat rolls down my face."
    "I've never done drugs, am I tripping right now? Did someone spike my Powerade while I was working and distracted?"
    "I feel myself being pushed."
    "I'm being moved, slowly, but it's noticeable."
    "My speed accelerates and I yell out in surprise."
    "Faster and faster, I keep moving until I can barely breathe due to the forces impinging on my body."
    "A very faint white light comes into view, coming closer and closer until it encompasses my vision completely."
    "I begin to slow down, almost to a standstill."
    "The spectacle lasts a while until, like clouds parting to let the sun shine through, the darkness opens up to lush green below." 
    "I feel the forces of gravity take hold of my body once again, and I begin to fall."
    "Down."
    "Down to ...somewhere."
label zecora:
    play music "mysterious.ogg"
    scene bg everfree with dissolve
    "I'm laying on the ground and something sharp is poking my leg."
    "Everything hurts."
    "Slowly, I begin to sit up and observe my surroundings."
    "Everything is marshy and I can hear frogs croaking and creaking."
    "Something {i}wriggles{/i} away."
    show zecora standing with Dissolve(0.5)
    play sound "hoofsteps.mp3"    
    "I hear a crashing and stomping through the brush."
    play sound "zecoraline1.mp3"    
    z "If minw eyes do not deceive, a strange being I do perceive!"
    "A striped horse with earrings and golden bangles around her waist approaches me."
    "I'm stunned into silence for several seconds."
    a "Oh my God, it's a talking horse!"
    "I just blurt that out with no forethought."
    z "A horse I am not; though I am close, in truth. I am a zebra, and my stripes are proof."
    a "Wha- who are you?"
    show zecora sit with Dissolve(0.5)
    play sound "zecoraline3.mp3"    
    z "Zecora is what they call me, now who might you be?"
python:
    povname = renpy.input("What is your name?")
    povname = povname.strip()

    if not povname:
        povname = "Anonymous"
    
a "My name is [povname]!"
z "[povname] then? I think we will be friends."
a "I'm glad to make your acquaintance, Zecora."
"You stick your hand out, as if to shake the strange equine's hand." 
"Before you can realize she has no hands to shake, Zecora puts a hoof in your palm and somehow delivers a firm, vigorous shake."
"With that, you stand up and out of the brush you found yourself in."
z "So tell me, friend, just when did that bush meet your rear end?"
a "Just now actually..."
z "I thought so, but I wished to check, for something has left these bushes a wreck."
a "I don't know how I got here. One moment I was in the bathroom, and then I was here."
z "That may be a mystery for another occasion, now come, stay close and avoid separation."
"She turns, and makes to head down a path that leads into the forest surrounding the swampy clearing."
"You follow her, the path soon becoming almost untraceable among into thorny vines and close trees."
show zecora stand with Dissolve(0.5)
z "Here in the Everfree, there are many beasts to flee."
a "What ...kind of beasts?"
z "Timberwolves and Cragodiles, foul creatures full of bile."
"Timberwolves and ‘Crag’-odiles?  Looks like I’m not in Kansas anymore."
a "I’ll make sure to look out for those."
z "No more need for you to roam. Now come, and I shall lead you to my home."
"I keep an eye on her so I don't lose her amidst the dense underbrush."
show zecora with Dissolve(0.5)
"Her striped flank and gray tail sway in front of me as I walk behind her."
"I notice certain things about her, like the fact she has outlines and the colors here are weirdly flat compared to where I just came from."
"Plus, a {i}talking horse{/i}..."
"What weird fairytale have I fallen into? Am I dreaming?"
a "Is this all a dream?"
play sound "zecoraline10.mp3"    
z "I do not know how strange this may seem, but this is assuredly not a dream!"
a "Really?"
play sound "zecoraline11.mp3"    
z "For you, this I speak true."
a "So I'm really not home anymore..."
"She didn't reply to that this time as I talked outloud to myself."
"Mud is caking my boots, and dirt is splattered on my jeans. My uniform is rumpled now."
"She looks back at me with piercing blue eyes."
play sound "zecoraline12.mp3"    
z "Don't worry your aching feet, our journey is nearly complete."
scene bg zecora tree with dissolve
play music "spooky.mp3"
show zecora back with Dissolve(0.5)
"She approaches a massive tree decorated with masks and bottles hanging from ropes."
"Zecora pushes aside some leaves and trots up to the door."
"She stamps her hooves to knock off detritus and goes inside, holding the door open for me."
"I have to bend down to go inside."
scene bg hut with dissolve
show zecora sit with Dissolve(0.5)
play sound "zecoraline13.mp3"    
z "Come in, come in, [povname] you are welcome here and have nothing to fear. Since Ponyville is farther away, here you will stay."
a "Thanks, Zecora."
"She goes to her pot in the center of the room and pulls out a big spoon."
play sound "zecoraline14.mp3"   
z "Hungry you might be after our trek, but I will take the time to check. If you are hungry for a meal, then I will make you a deal."
a "A deal?"
play sound "zecoraline15.mp3"    
z "Trade me some of your clippings of nail, for future spells without fail."
a "Well, that's a little weird but okay."
"She passes me some nail clippers in an anatomically-impossible fashion with her hoof. I take them and do as she asks, clipping my fingernails."
a "Uh, you're not going to be casting these future spells on me, are you? Or cursing me?"
show zecora front with Dissolve(0.5)
play sound "zecoraline16.mp3"    
z "No, such a thing I would not do, or my luck would be shot through."
"She collects the fingernail shavings, humming to herself, and then puts them in a jar."
show zecora with Dissolve(0.5)
play sound "zecoraline17.mp3"    
z "I am a collector by nature, now let me label it by nomenclature. What manner of creature are you, just between us two?"
a "I'm known as a human."
"I say it with a slight grimace. This is all so silly. Any minute now, I'd surely be whisked back suffering from a headache..."
"Any minute..."
"She writes the word in ink with a feather and a flourish."
play sound "zecoraline18.mp3"    
z "As agreed, I will prepare dinner for us, so simply wait there without a fuss."
scene zecora stir with dissolve
"She starts a fire under a huge black pot with some flint."
"Zecora puts in a bouillon cube, chopped vegetables, canned corn, noodles into a big pot."
"She pulls out a ladle and stirs the soup."
".{w}.{w}."
"Time passes."
scene bg hut with dissolve
show zecora with Dissolve(0.5)
"Zecora gets two bowls, two spoons, ladles out the hot soup into the bowls, and puts them on the table. I pull up an extra chair and sit down at the table."
"I'm having supper with a talking witch zebra."
"This is my life now..."
"I dip my spoon in and eat some of the soup."
"She's watching me."
show zecora sit with Dissolve(0.5)
play sound "zecoraline19.mp3"    
z "[povname], is it good to eat? Self-grown veggies are for me a treat!"
a "Yeah, it's good! Very savory."
"I chew the pasta noodles with gusto. The vegetables are mixed in and the broth is decent. Very tomato-ey."
a "Mmmm."
play sound "zecoraline20.mp3"    
z "The carrots are the hardest to grow, but they are my favorite though."
a "I see. Is it hard to always speak in rhyme like that?"
play sound "zecoraline21.mp3"    
z "Practice makes for perfection, rhyming becomes a natural skill with some direction."
"I empty my bowl and the grey zebra takes it and places it in the sink with hers. She washes them. I start to protest but she shakes her head."
show zecora with Dissolve(0.5)
play sound "zecoraline22.mp3" 
z "As a guest, it would not do. Sit back, relax, and I will find a place for you."
"She smiles at me after scrubbing the bowls with soap and rinsing them and placing them on a towel."
play sound "zecoraline23.mp3"    
z "I have just the thing, just you wait, it's like I knew you were coming through fate."
"She pulls out some bit of cloth, unrolls it, and attaches it to rings on the wall and the roof."
"After she's done, I realize she's hung up a hammock for me."
a "Thank you. I'm not ready to lie down yet."
play sound "zecoraline24.mp3"    
z "It's good to be ready, you do look unsteady."
a "I do?"
"She's right, that walk must have taken more out of me than I thought. I sit in one of her chairs."
"Hmm..."
"I look around..."
"No television here..."
a "What do you do to pass the time around here?"
play sound "zecoraline25.mp3"    
z "I often read a book borrowed from Twilight, when it comes to the night."
play sound "zecoraline26.mp3"    
z "Speaking of her, on the morrow, we'll visit her since with mysteries, she is most thorough." 
a "O-oh, okay. Do you have a book I could read?"
show zecora back with Dissolve(0.5)
play sound "zecoraline27.5.mp3"    
z "Many such books, if you want to take a look."
"She gestures to her bookshelf, inviting me to head over."
"I take a deep breath, and pull out a random book off the shelf."
"It's a book about pony magic. I start reading it but it doesn't really make sense to me."
"I try the next one."
"It's a book with a blushing pony on the cover in the arms of a stallion. I leaf through it experimentally."
show zecora stand with Dissolve(0.5)
play sound "bookcover.mp3"    
z "Oh, that is a good one, reading it will be fun. Don't judge the book by its cover, it's a tale of adventure about her lover."
"You know, what the hell. I never read these but maybe a horse romance could be interesting."
"First day in a new world, after all."
"I sit down in one of her chairs and read through it."
"At first, I'm not taken in. It just reminds me of my first girlfriend, who used me for my car and job and I'm thinking about that instead."
"Eventually, I get caught up in the drama. Her husband is actually a time traveler and he has to get them back to their original time period."
"She has to take up arms to defend him and learn how to time travel herself."
"It definitely wasn't what I expected."
"I don't finish it, I only get about a quarter of the way through before I start feeling tired."
"I give a big yawn."
a "Hey, I'm going to bed now."
show zecora sit with Dissolve(0.5)
play sound "goodnight.mp3"    
z "Have a good rest and goodnight, be sure to sleep tight."
scene black with dissolve
"I climb into the hammock she's hung and she comes over to give me a pillow."
"I'm swinging slightly from side to side. The linen fabric of the hammock is soft enough."
"I punch the pillow to soften it, which she watches perplexed and then lay my head down on it."
"Zecora does something with some natural material, sorting it."
"It's quiet enough and the light is low, except for her candle."
"Still, I toss and turn from side to side."
"I have trouble getting to sleep or, rather, relaxing."
"At some point, I'm experiencing something weird."
"It's familiar snippets."
"It's after I've moved into my new apartment and I've been living day to day with no ambitions."
"My girlfriend left me, my family doesn't talk to me and I'm on unemployment."
"Half my stuff is still in boxes, untouched. I just get it out of the box when I need it."
"In my dream, I trip over a box and it spills open, releasing more boxes around me."
"The walls close in."
"Then this weird presence comes in and everything goes back to how it was before."
"I'm left in an empty apartment."
"Suddenly..."
"In the morning, a gentle touch wakes me."
show zecora front with Dissolve(0.5)
play sound "notbeen.mp3"    
z "Now is the time we must walk again, and go where you have not been."
scene bg everfree with dissolve
"The sun is barely piercing the trees outside and a gloomy fog clings to the ground."
"You walk beside her."
"Once again, you wished you had a pair of boots on."
"Well, it's not as far as when you first ran into Zecora."
scene bg ponyville with dissolve
"The trees break and you see a quaint little town with yellow roofs for the first time."
jump meetingtwilight

label meetingtwilight:
    play music "chill.mp3"
    scene bg library day with dissolve
    "We walk through the streets and ponies gawp at us." 
    "Well, no, me. They gawk at me."
    "Zecora stops in front of what I assume is our destination."
    "There's a massive tree here formed into a house with windows and doors directly in the trunk."
    "Zecora leaves me to marvel at this impressive natural structure while she hammers a rhythmic knock onto the door."
    
    "While you two are standing in the street, a pink pony with a poofy mane walks up."
    show pinkie gasp with Dissolve(0.5)
    "She sees you and gasps loudly."
    hide pinkie gasp with dissolve
    "Then she runs away."
    "Oh no."
    "Even the locals here are frightened of you because you're not a cartoon pony like them."
    show twilight hoof with Dissolve(0.5)
    t "Coming! Coming!"
    "The door opens to reveal a rather frumpy and exhausted face on the other side."
    "A purple pony! A unicorn to be exact. She eyes me up and down, politely restraining the thousands of probing questions that are likely running through her mind right now."
    hide twilight hoof with dissolve
    show zecora stand with Dissolve(0.5)
    play sound "zecoraline27.mp3"    
    z "I found this traveller lost in the Everfree, I thought you might like to see."
    hide zecora with dissolve
    "She realizes that gawking at me probably isn’t all that polite, shaking herself out of the momentary trance and extending a hoof in greeting."
    show twilight surprised with Dissolve(0.5)
    t "Gosh, where are my manners? I’m Twilight Sparkle, and I’m... actually in the middle of... "
    show twilight annoy at left with Dissolve(0.5) 
    t "SPIKE! {w} SPII-IIKE! Have you seen my copy of Enigmatic Enchantments and Cryptic Curiosities?"
    "She’s clearly pretty preoccupied with something. Looks like she hasn’t had a good night’s sleep in weeks."
    "The frazzled mane, the twitchy eyes... I can’t even see a lick of sunlight in this stuffy treehouse of hers behind her."
    show zecora at right with Dissolve(0.5) 
    play sound "zecoraline28.mp3"    
    z "Perhaps now is not a good time? My friend here is lost and we thought that you might f-"
    show twilight surprised with Dissolve(0.5)
    t "Oh, no no no! Now’s a perfect time Zecora, and... Shoot, I didn’t even ask you your name!"
    a "It's [povname]!"
    t "[povname]. Very interesting. Please come in! Make yourself at home!"
    play sound "zecoraline29.mp3"    
    z "If Twilight approves, I leave you to be safe in her hooves."
    "She leaves out the door."
    hide zecora with dissolve
    scene bg library
    "I sense this place has seen better days. The books have been carelessly tossed about the floor."
    "It looks like a bomb just went off in here! There’s a shrine of empty coffee cups and open books on one side of the room, which I assume is Twilight’s workspace."
    "With the absence of sunlight or air circulation inside the library, I’m not surprised that Twilight is as agitated as she is."
    show twilight hoof with Dissolve(0.5)
    t "Sorry, this place is a real mess, I wasn’t expecting visitors and..."
    "She babbles to herself as her magic sets to work clearing away some of the books and chaotically-arranged paper piles."
    "I have to stop for a second just to observe it. Real magic!"
    "White sparkling clouds of the stuff envelop the items scattered around the table. "
    "Among the many books and half-empty coffee mugs is a little tattered pony ragdoll that Twilight quickly hides away in a chest with the rest of the clutter."
    "A small dragon hands her a book and she places it on her desk with magic."
    "The purple unicorn turns her full attention on me."
    "Twilight takes her time, enthusiastically circling me."
    "She examines every inch of me."
    "Well, nearly every."
    "I can't help but feel a little naked, despite the fact I'm wearing clothes."
    "My eyes fall on the one decidedly named Spike. He stares back and shrugs, seemingly uncaring for the time being."
    t "Holy cow, so you are bipedal, huh? And none like any I've ever seen. Well, except monkeys, but you are definitely different."
    a "Yeah, it's pretty bog-standard where I'm from."
    "She stops circling me."
    t "Where ARE you from, anyway?"
    "She is far too excited about this."
    a "I'm from... Wait. Where are WE then?"
    "She tilts her head questioningly. She must think I'm crazy."
    "Hell, maybe I am. All I see around me are pastel-coloured ponies!"
    "Well, that and a zebra, I suppose."
    t "We are in Equestria, but judging from the way you reacted I'll have to assume you have never heard of anything like this before."
    "She's perceptive."
    "I nod."
    "She raises a hoof to her chin and leans a little closer towards me, eyes narrowing."
    "I'm a little uneasy, having her stare so intently into my eyes."
    t "your claws are flat and short."
    a "Is that important?"
    t "Well, I, uh..."
    "She reverts back to her original position, satisfied with her analysis."
    "Twilight turns to Spike."
    t "Spike, take a letter, please." 
    "Spike procures an empty piece of parchment from... somewhere."
    t "Dear Princess Celestia, I write to you today not on the subject of friendship, but on the subject of a more serious matter."
    t "Zecora has come across a strange... creature, resembling a monkey, except it can talk, and it walks on two legs!"
    "Princess?! What sort of place is this? Run by a princess?"
    t "Please respond as soon as possible, I have no idea what to do with it! Your faithful student, Twilight Sparkle."
    a "Ahem, I am a human, thank you very bloody well much."
    "She laughs nervously."
    t "Sorry about that. A human, you say? Interesting..."
    t "You have forward-facing eyes? Are you a predator?!"
    a "Uh, no."
    "She jots this down on a parchment she has sitting on a table in the middle of the room, being full of notes already."
    t "Spike! You can send that letter now."
    s "Okay!"
    "Spike then wraps up the parchment, holds one end by two claws, takes a breath and breathes a small green fire at it."
    "The parchment is nowhere to be seen."
    "I jumped back in surprise."
    a "What the hell was that? Why did you burn that letter?"
    "Twilight laughs at my question."
    t "Oh no, he didn't burn it. He sent it to the Princess using magic!"
    "Oh. Great. Magic."
    "Don't gotta explain shit, I suppose."
    a "Sure, okay."
    "I find myself with nothing to say. My mind is reeling with so many questions it's overwhelming. So I just stand there feeling a little awkward, waiting for the Princess's response."
    "Twilight seems to be in a similar position, having exhausted her seemingly endless supply of questions about my physical attributes."
    "Spike, seeming bored, gets up and begins to clean the place up, opening a window and letting the stale air flow out." 
    "I finally found something to say."
    a "...I'm not going to get killed, am I?"
    "I didn't really think I was going to be killed, but I thought asking a serious question would be met with a serious answer."
    "Twilight looks at me a little surprised."
    t "What? Of course not! Celestia wouldn't dream of killing what could be the very first of a brand new species!"
    "I suppose I can be satisfied with that. "
    a "Err... do you mind if I sit?"
    t "Oh no, not at all, please take a seat. Sorry about that, I got too excited."
    a "You're not wrong there, Twilight."
    "Christ, I just said Twilight, in reference to the name of a goddamn talking magic pony."
    "I sink into the seat, sighing long and heavy, and closing my eyes."
    a "I'm gonna get some rest..."
    "I hear no response, so I assume Twilight and Spike are letting me have my rest."
    scene black with dissolve
    "The only sounds I hear is the soft breeze coming from the opened window, and what I assume to be Spike cleaning up the place."
    "What even is this world..."
    "Sleep came hard again that night."
    "The same strange experience, but with a different conclusion."
    "Dreaming again, back home again. There's screaming, yowling."
    "My body is shuffling in the bed, while back then I was flailing mad."
    "She wouldn't listen. I wouldn't back down."
    "The carrier under her arm is practically shaking."
    "Whatever is inside isn't my cat. It wants to hurt me."
    "The door springs open, just as our screaming match hits a climax."
    "This time that odd presence isn't what ends the dream..."
    "It's the rage."
    "By the time I realize I'm awake I've already been screaming out loud for a few seconds."
    a "SHUT UP!!!!"
    "A gasp nearby, sounding hurt."
    t "What's wrong, [povname]?"
    a "Ah... just a bad dream, sorry. It was nothing."
    t "Didn't sound like \"nothing.\""
    "There's a pregnant pause."
    t "You know you can talk to me if you're ever u-"
    a "No, I'm fine. Really. Maybe some other time."
    "I stand up from the plush chair and stretch."
    a "How about breakfast and coffee?"
    t "Okay. What do you eat for breakfast?"
    a "A couple scrambled eggs?"
    t "Ah, so you do eat meat! I wasn't sure because your teeth are flat. Well, we have some eggs for baking but I- {w} oh, I'm rambling. Let me get you fed."
    "She leads the way to the kitchen."
    "She gets some eggs, butters a pan, and whisks them then cooks them until the clear goop is white."
    "She plops them onto a plate, salts it, and serves me with a smile."
    t "Eat up, [povname]! You have to eat all the eggs. You've looked so tired and you need your energy!"
    "She's bossy, but it comes from a warm place."
    "Spike comes into the kitchen in an apron and starts cleaning the pan in the sink."
    "It brings back unpleasant memories for me."
    "Twilight puts on a pot of coffee."
    "The brown liquid trickles down through the filter."
    t "How do you take it?"
    menu:

        "Black.":
            jump blackcoffee

        "With milk.":
            jump milkcoffee

        "With cream and sugar.":
            jump creamsugarcoffee
            
        "Extra sugar":
            jump sugarcoffee

label blackcoffee:
    a "I'll take it black, thanks."
    "Twilight pours some coffee in a cup and hands it over to me."
    jump twilight2
label milkcoffee:
    a "I'll take it with milk, thanks."
    "Twilight pours some coffee in a cup, adds some milk, and hands it over to me."
    jump twilight2
label creamsugarcoffee:
    a "I'll take it with cream and sugar, thanks."
    "Twilight pours some coffee in a cup with creamer and sugar and hands it over to me."
    jump twilight2
label sugarcoffee:
    a "I'll take it with extra sugar, thanks."
    "Twilight pours some coffee in a cup, pours in two teaspoons of sugar, and hands it over to me."
    jump twilight2
    
label twilight2:
    t "Here you go, [povname]."
    a "Thanks, Twilight."
    "My hand brushes her hoof as I take the cup."
    "She blushes a little."
    a "Oh, sorry."
    t "Don't be, I don't expect you to be perfect at everything on the first day of being in a new place."
    s "Yeah, just like you Twilight, right?"
    "She giggles nervously."
    t "You just had to bring that up, huh?"
    "She clears her throat."
    "Spike winks at you."
    "I look away suddenly, sipping the coffee."
    "Oh, yeah, and your eggs. You didn't eat them yet. You shove a bite in your mouth."
    a "Mmm, this is really good."
    "She brightens."
    t "It is?"
    a "Yup."
    "Behind us, Spike burps and a letter hovers in mid-air for a second that he grabs."
    s "Hey! Celestia is on her way, she says!"
    t "O-ooo. I don't feel ready. Do you feel ready?"
    "She frets."
    "I put a hand on her shoulder, without thinking."
    a "You'll be fine."
    t "R-really?"
    a "Definitely."
    "Time passes."
    

label celestia:
    scene bg ponyville with dissolve
    "Twilight escorts me into the center of town, and finally I have a chance to get a look at the hustle and bustle of Ponyville proper."
    "It’s very quaint. Couldn’t be further from life back home." 
    "No chugging of machinery or roar of car engines. No smoke or pollution or piss-stained alleys."
    "The buildings are thatch-roofed, quite a bit smaller than I’m used to. I’d have to stoop just to step through the front door."
    "Along with the homespun architecture seems to be a pervasive friendliness."
    "Even though I’m a gangly five foot ten freak, ponies greet me cordially as I pass them by."
    scene bg market with dissolve
    t "Princess Celestia is just... oh, she’s... just amazing! She’s my mentor and ALSO the most important being in Equestria, just saying..."
    "The way Twilight is freaking out suggests we’re on our way to meet a celebrity rather than a monarch, and the banners, stalls and assembly gathered in her honor only cement this assumption."
    "Wow. Celestia really has these ponies’ respect. She’s clearly the big cheese around here."
    "Or... the big cake. Damn."
    "I stop dead in my tracks before I end up stumbling face-first into the royal rump."
    "Sensing someone behind her, Celestia springs to attention and turns to greet us both."
    show celestia happy with Dissolve(0.5)
    c "Twilight Sparkle! My most beloved student! How good it is to see you again."
    "She turns to face me, and the moment her eyes lock on I melt a little inside. Her pink eyes are arresting, and her pastel mane waves gently in the air."
    "Celestia’s nibbling on a wedge of chocolate cake, and even while doing something so casual she exudes authority and grace."
    "I feel an impulse to kneel just being in her presence."
    show celestia smile with Dissolve(0.5)
    c "And you must be dear [povname]."
    "She bows her head respectfully."
    show celestia happy with Dissolve(0.5)
    c "Twilight wrote to me about you, though I sense her letter was dispatched rather hastily. I noticed three spelling errors."
    "She smirks to the trembling unicorn by your side."
    hide celestia happy
    show twilight surprised with Dissolve(0.5)
    t "Sorry! Sorry, Princess! I was just in such a hurry to inform you about Anon and I-"
    hide twilight surprised
    show celestia smile with Dissolve(0.5)
    c "Worry not." 
    "She silences Twilight with a gentle wave of her hoof."
    c "I've already taken care of things. I stayed up to make a welcome packet for you on Ponyville customs and other information you'll need."
    "She hands you a folder with multiple pages."
    a "Wow, thanks."
    "She smiles shyly."
    show celestia happy with Dissolve(0.5)
    c "For a new subject, it is my duty to make sure your transfer is as smooth as possible. In that regard, I have more news."
    t "More?"
    c "I've arranged for Pinkie to welcome you here with a party on your behalf so you can meet everyone."
    t "Gee, that sounds {i}awfully{/i} familiar..."
    show celestia giggle with Dissolve(0.5)
    "Celestia giggles knowingly."
    c "Doesn't it, my student?"
    "She raises a hoof to her mouth."
    c "He'll be following in your footsteps."
    t "Good."
    a "So, while you're here: I have a question. You're the ruler, right?"
    "She hesitates."
    show celestia happy with Dissolve(0.5)
    c "Co-ruler. Of the day mainly."
    "I don't really know what that means."
    a "So, some ponies have horns and some wings and I guess some. like you, have both? What does that mean?"
    c "Earth ponies, the ones without, specialize in being strenth and growth of natural things. Unicorns specialize in magic and pegasi deal with weather manipulation."
    "She takes a breath."
    c "As for me, I have special powers over the sun and sky and other things."
    a "Wow."
    c "Tell me, Anon- what are humans like? Are they like us?"
    a "Well, people ... multiple humans, I mean... they work jobs and things according to their skills. I suppose that's kind of like that."
    c "I would love to hear more sometime. You know, you're welcome to come to Canterlot anytime. Just send the word through Twilight and I'll have a chariot sent for you."
    a "Oh, hmm. Well, you said there was a party first, right?"
    c "That's right! I'm sure you're have a wonderful time, my subject."
    "I don't know how to reply to that, being someone's 'subject.'"
    "So I don't say anything at all."
    t "Princess, if I could have a moment of your time?"
    "She goes away to talk with Celestia separately."
    "It gives you time to just look around and take things in again."
    "You open the folder and start reading the packet."
    "There's a map of Ponyville and it's annotated with personal notes and addendums."
    "As you're reading it, Celestia finishes talking to Twilight and comes back. She's looking over your shoulder."
    "She points to a spot on the map."
    c "Right there is Sugar Cube Corner, where your party will be taking place today at 4 PM. Don't be late!"
    t "Oh no! I'll make sure he makes it there on time!"
    c "Right, well, I'll see you there!"
    a "Right... "
    
label preparty:
    scene bg library with dissolve
    t "Pinkie's parties are just the greatest!"
    "Twilight exclaims to me, hiding no excitement in her voice or gestures."
    "Waving her hooves around, trotting around her home in excitement, droning on about the sort of party games they play and songs they sing."
    "She nearly bumps into Spike while he is still cleaning."
    s "Oof."
    "Poor bastard."
    t "We haven't had a party in a while, I kind of miss them!"
    "It's hard for me to concentrate on the conversation."
    "I don't want to be rude though."
    "So I ask a question, in an attempt to re-engage myself in the conversation."
    a "Since this is a party, how many ponies are going to be there? At Sugarcube Corner?"
    t "Everypony, of course! You are going to meet so many new ponies at this party."
    "I just recalled something."
    a "This Pinkie. Does she have pink hair and skin and blue eyes?"
    "It has to be her, surely."
    t "Huh? Oh, you mean mane and fur."
    a "Whatever."
    t "Yes, that's her. So you saw her then?"
    "I nod."
    a "Yeah. She, like, jumped into the air, and practically flew away."
    "Twilight nods like it's normal."
    t "That's just how she is, Anon. Ever jubilant and energetic."
    "I guess it's normal."
    "Christ. I wonder what she'll be like in-person."
    "In pony...?"
    "Fuck this shit."
    "I let out a sigh as I stand up."
    a "It's nearly time, right?" 
    "I point to the clock on the wall."
    "3:46 PM"
    "Twilight turns to face me."
    t "Oh shoot, you're right!"
    "The impressions she's leaving on me are leading me to believe she's not very organised... "
    "But perhaps that's due to circumstances outside of my knowledge."
    "I'll try not to form any opinions too early."
    a "Do I need to bring anything?"
    "I ask as a sort of formality, more than anything."
    t "Only yourself."
    "Twilight grins."
    a "Should I get this Pinkie a card?"
    t "I've got a blank card you can sign, [povname]."
    "I return with a smirk of my own."
    a "So I don't neeed to bring the stuff Celestia gave me?"
    t "You shouldn't need it, Spike and I can take you there and back."
    t "Spike! It's time to go to the party!"
    scene bg market with dissolve
    "Twilight dashes out the door in unrestrained elation."
    "I follow behind her while Spike puts away his cleaning tools and comes out shortly after I leave."
    "Twilight closes the door with her magic and begins heading towards where Sugarcube Corner must be."
    "I fall in line, walking beside Twilight with Spike on her opposite side."
    "I notice a few ponies also heading in the same direction."
    "Fair enough, it is near the centre of town after all. "
    "I can't help but feel a sort of aura around this town."
    "An aura of welcoming and comforting pleasantness that encompasses everything. Like an Amish community or something."
    "It leaves a warm feeling in my heart, and I involuntarily smile."
    "Heh. This place ain't too bad."
    scene bg fountain with dissolve
    "We pass a corner and the street opens up to a large courtyard, with a big fountain near the middle."
    scene bg sugarcube with dissolve
    a "I'm just going to go ahead and guess that massive candy looking building is our destination?"
    "I point as I ask."
    t "Indeed it is!"
    "It sticks out like a sore thumb."
    "A really sore thumb."
    "That's when I notice it. "
    "Droves of ponies entering Sugarcube Corner."
    a "Wait. Pinkie invited everyone?"
    t "She always does. That's how she operates when a new pony moves into town."
    a "Literally everyone?"
    t "Literally everyone."
    a "Huh. Okay then."
    "By the time we finished our conversation, we ended up out front."
    "Twilight loses herself and practically leaps through the door, obviously excited to get to partying."
    "Recalling the state of her library, I didn't expect her to be like this."
    "I expected a more recluse and self-isloating type of personality, from what I've seen back on Earth."
    "These were the traits these types of people exhibited."
    "But Twilight seems different."
    "I'm almost certain I caught her at a bad point in time."
    "I turn to Spike, who hadn't followed Twilight in."

label party:
    a "It's not going to be too crazy in there, right?"
    s "Well you definitely don't know Pinkie Pie, then."
    "Spike heads in with a thumbs up and a smirk."
    "I let out a heavy sigh."
    a "I sure hope I don't die in here."
    "The chattering, music and shuffle of hooves coming from inside the building wracks my nerves a bit."
    "Come on, Anon. You got this."
    "I step inside."
    "I make it a few steps into the building."
    scene bg sugarcubecorner with dissolve
    "I'm assaulted by some kind of burst or spray in my face."
    "I gasp."
    "It's ... confetti?"
    "Wow, there are so many ponies!"
    "I catch a blur of pink movement and out of seemingly nowhere, that pink pony I saw earlier appears in front of me."
    p "Hey!"
    "She exclaims."
    "Holy shit!"
    "I stumble backward and fall on my backside."
    "What the hell was that? Super speed?"
    "All the other ponies laugh at the spectacle."
    "Ah man, that's embarrassing."
    "Quickly picking myself up, I address the pink one."
    a "Uh, hey there. Pinkie, right?" 
    "She gasps again."
    "Christ..."
    p "Wow you already know my name you're really on the ball I haven't even gotten to know your name yet-"
    "It keeps on going."
    p "I've been so busy organizing and inviting everypony since yesterday I saw you and I went *GASP* because I've never seen anypo- anything like you so you just had to be new and I always throw a party for every new resident of Ponyville!"
    "..."
    "What the fuck..."
    "She's panting, having said that all in one breath."
    "I chuckle, still feeling embarrassed after making such a spectacular entrance and instantly becoming the center of attention."
    "Pinkie set this up all for me. Someone she had literally never seen before."
    "There's that feeling again. That warmness in my chest, and a friendliness that permeates the room. Smiling ponies all around, happy to see me."
    "I end up grinning, past embarrassments already placed behind me."
    a "Well. I really appreciate it, Pinkie... Pie? Was it?"
    "I stick my hand out, and she takes it with both hooves and and with a grin to match my own, she shakes it rapidly, leaving me a bit rattled."
    "She nods multiple times."
    p "Yes indeedy daring do!"
    "She chirps back."
    "I really appreciate this. Seriously."
    p "Anything to get a smile, Anon! Make sure to have lots of fun!"
    "Most ponies have already moved past the commotion that was Pinkie Pie \"welcoming\" me and were mingling with their own."
    "I guess I'll find someone to talk to. But first, I'm hungry."
    "I wade through the crowd of ponies towards the table filled to the brim with traditional party snacks."
    "Cupcakes, muffins, cookies, a few cakes and even a bowl of punch."
    "I grab a cookie and pour myself a cup of punch, while turning to face away from the table, gazing out into the crowd."
    "Wow, these are so good!"
    r "I know, right? Normally I do not partake in sweets but I will always make an exception when it's a party of Pinkie's calibre."
    "I turn to see a stunningly pristine white coloured unicorn pouring herself a cup of punch with her magic. "
    r "Might you be so kind as to pass me one dear?"
    "I oblige, handing her a cookie which she grabs with her magic and takes a small bite."
    r "Why thank you.. [povname], was it?"
    a "That is me. [povname]."
    r "How wonderful it is to meet you, [povname]."
    a "I'm sorry. What is your name?"
    "She points a hoof to herself."
    "My name is Rarity. I design dresses at the Carousel Boutique. Fashion is my everything."
    a "You run an entire business yourself? Damn, that must be some good money."
    r "Oh, I get by."
    "Out of the corner of my eye, I spot Spike approaching us."
    "He looks as if he's in a trance."
    "Must be hungry, poor guy was working all day no doubt."
    "Spike stops in front of Rarity."
    s "H-hi Rarity."
    r "Good evening, young Spike."
    "She takes another bite."
    "Spike pauses and turns to me."
    s "Oh, and hi Anon."
    "I give him a small wave."
    a "Hey buddy. You hungry?"
    "I grab yet another cookie and pass it to him."
    "He shakes his head slowly, like he's stoned."
    s "Absolutely, thank you!"
    "He greedily eats the entire cookie in a single bite, much to the apparent disgust of Rarity, who recoiled slightly at the sight."
    "Spike notices her reaction, and wipes his mouth of any remaining crumbs."
    s "Oh. Whoops. Sorry Rarity." 
    r "That's okay, dear." 
    "She trails off."
    "She's not okay with it."
    r "Well I'm afraid I must be getting along now. [povname], it was nice meeting you. Hopefully, we will see each other around sometime, yes?"
    "I nod."
    a "Yeah, sure. Of course! I'll see you 'round."
    r "Good day to you both."
    "She trots off into the crowd, leaving Spike and myself at the table."
    "He sighs."
    a "What's wrong, Spike?"
    s "I think I just scored a negative on the attraction scale... "
    "Wait."
    "Spike likes Rarity?"
    a "That's alright. Maybe next time, tiger." 
    "I attempt to console the baby dragon."
    "Damn, I'm no good at this. Spike just sighs again, not hearing my words of encouragement."
    s "Yeah, maybe... I'll catch you around, Anon."
    "With slumped shoulders, Spike disappears into the crowd."
    "Sorry, little guy... I tried."
    "I gaze out into the crowd, and my eye catches a rainbow-like mane making exaggerated movements while talking really loudly."
    "This pony seems interesting."
    "As I approach I can hear snippets of the conversation."
    rd "So I cleared them all, and, as I said, in ten seconds flat! You should've seen the look on Twilight's face."
    "The rainbow-maned pony laughed."
    "Despite being much louder and bombastic than everyone else in the room, it seemed that only one pony was paying attention to her."
    "A yellow pony with pink hair was nodding along with the story."
    "I couldn't see her face, as she was facing away from me."
    "The rainbow one notices me, and shouts:"
    rd "Oh, hey, it's the monkey!"
    "At this shout, the yellow one jumps and turns around to face me, seemingly hiding herself behind her mane and lowering her head."
    a "Uh, no. I'm a human, not a monkey, and my name is [povname]!"
    "I'm getting a little sick of having to say it every time."
    rd "Yeah yeah, whatever you say. My name's Rainbow Dash, and this one is Fluttershy. Nice to meet ya!"
    "As Rainbow says this, she moves up next to Fluttershy and puts a foreleg around her shoulder. She blushes a bit and relaxes."
    "Must be pretty damn shy... Fluttershy..."
    "Yeah okay. I guess Rainbow Dash fucking dashes everywhere too."
    a "You are both pegasi, huh?"
    "Rainbow gives a cocky smirk."
    "Yep, the fastest pegasus in Ponyville, and the most athletic!"
    "Right on the money..."
    a "Really? That must be pretty fast."
    rd "Oh, you know it. Wanna come watch me sometime?"
    "I don't have any reason to say no."
    a "Sure. That sounds good to me."
    rd "Yes!" 
    "Rainbow Dash jumps a little in excitement." 
    "It would be pretty interesting to see a flying talking creature after all."
    rd "What about you Fluttershy? Wanna come watch me do tricks for Anon?"
    f "U-um... Yes, please..."
    "Very shy."
    rd "Great, I can't wait!"
    "Rainbow Dash takes a step forward."
    rd "Well, it was nice meeting you, Anon. You seem pretty cool. I hope to see what tricks you can do, if any."
    "She raises a hoof and holds it out to me."
    "I reach out and shake it, but she pulls away, and sticks out her hoof again."
    rd "No, Anon, you gotta bump it!"
    "I ball my open hand into a fist and bump her hoof."
    "It was kind of soft. It was nice."
    rd "I'm gonna grab some punch. I'll catch you later, Anon. Bye, Fluttershy."
    "Fluttershy timidly waves."
    f "S-see you later, Rainbow."
    "I'm left alone with Fluttershy."
    a "So, Fluttershy... What do you do for fun?"
    "Awkward..."
    "She plays with her hoof, dragging it across the floorboards."
    "I cough."
    a "So yeah... You're friends with Rainbow?"
    "I hear a whimper from her mouth."
    "Adorable."
    aj "Howdy partner!"
    "I turn to the voice, and I see an orange coloured mare wearing a typical cowboy's hat."
    "Southern accent, cowboy hat... {w} Is she a wrangler or something?"
    "I wave."
    a "Hey there. Name's Anonymous. What's yours?"
    "She takes her hat off (with her hoof?!) and does a sort of curtsy."
    aj "The name's Applejack, mighty fine to meetcha!"
    "She doesn't waste any time as she suddenly grabs my hand and shakes it firmly."
    "Ow, a bit rough."
    a "Likewise."
    aj "I see you already introduced yourself to Fluttershy and Rainbow Dash."
    "She's an energetic one, that's for sure."
    aj "Yeah, she can be like that. It's what makes her her, you know?"
    a "I get it."
    "Applejack is much easier to converse with than Fluttershy. I glance at her for a moment."
    "She seems a bit more relaxed at the moment, but perhaps still too hesitant to engage in conversation."
    "I don't want to push it."
    a "So. Everybody here knows each other?"
    "Applejack nods."
    aj "We're a real tight-knit community. We all care for each other."
    a "Good to hear."
    "Applejack turns to Fluttershy."
    aj "C'mon, Fluttershy. You gotta at least say something. He doesn't seem mean at all!"
    "Applejack gives her a warm smile."
    f "H-h-hello, Anon."
    "Goddamn adorable."
    a "Hey there. Are you enjoying the party?"
    "I try to speak as soft as I possibly can while still being heard above the hustle and bustle of the music and chattering ponies."
    f "Y-yes, I am. Thank you for asking."
    "Help. I think my heart is melting."
    "Applejack pats her on the back."
    aj "That's the way, sugarcube. See? You'll both be great friends in no time!"
    "Fluttershy smiles a little."
    "Out of nowhere, a particularly pink pony jumps up onto an empty table."
    p "Okay everypony! It's time to play some games!"
    "The room falls to the level of whispers."
    p "Applejack! Where are you?!"
    "She yells, her eyes scanning the room looking for the cowgirl."
    "Applejack raises a hoof."
    aj "I'm right here, Pinkie! What do you need?"
    p "The apples I asked you for apple bobbing, silly!"
    aj "Oh, right. Let me go grab the sack I brought with me. One moment Pinkie!"
    "Applejack goes to a corner of the room and returns with a sack of what I assume to be apples inside."
    p "Great! Just dump them into the big bucket over there!"
    p "The other game tonight will be... pin the tail on the pony!"
    "The crowd cheers."
    "Must be a favourite."
    p "And our first contestant will be... " 
    "Pinkie waves her hoof around the crowd."
    "And around..."
    "And around..."
    "She's making weird sounds."
    "She finally lets her hoof fall towards...{w} me."
    a "Me?!"
    p "Uh-huh! This party is for you and I doubt you've ever played pin the tail on the pony so I want to see you how you'll go at it!"
    "Eh, fuck it. I'll take it in stride."
    "I puff out my chest, and put my hands on my hips."
    a "I may have never played pin the tail on the pony but I never turn down a good challenge!"
    "The crowd erupts again, pleased with my gusto."
    "This is going to be a great night indeed."
 

    call screen party
    
    
label pinkieparty:
    "You decide to hang out with Pinkie."
    
label dashparty:
    "You picked Dash."
label spikeparty:
    "You picked Spike."
label twilightparty:
    "You picked Twilight."
label rarityparty:
    "You picked Rarity."
label fluttershyparty:
    "You picked Fluttershy."
label applejackparty:
    "You picked Applejack."

#This needs to be expanded.
"We played pin the tail on the pony and bobbed for apples the rest of the night."
    
label lyra:
    scene bg bench with dissolve
    show lyra happy with Dissolve(0.5)
    play sound "LyraLine1.mp3"    
    l "...So what do you think? Surely you are hungry by now, it's nearly noon!"
    "Lyra positively beams at you."
    "You planned on going to ask Pinkie if she needed help with anything today, but a short detour to grab a snack with a friend won't hurt, right?"
    "You shrug."
    a "Sure, I've got time. Where's the venue?"
    show lyra hop with Dissolve(0.5)
    "Lyra jumps in excitement." 
    play sound "LyraLine2.mp3"    
    l "This way! This way!"
    show lyra hoof with Dissolve(0.5)
    "She turns and at a brisker pace than usual, trots towards her intended location."
    "Is she excited?"
    "Why? It's just lunch."
    "You scratch your head, trying to keep up with her quickened pace."
    scene bg diner outside with dissolve
    "You arrive at the restaurant."
    scene bg diner with dissolve
    play sound "LyraLine3.mp3"
    show dinertable
    show lyra hoof behind dinertable with Dissolve(0.5)
    l "Oh, here! This table!"
    a "Wait... Lyra. That table already has stuff on it, we can't take that."
    "And it looks strangely fresh, too. The glasses of milkshake don't even have condensation on them yet."
    play sound "LyraLine4.mp3"    
    l "Oh, that's fine! I ordered ahead of time, it's actually for us!"
    "She turns and beams at me again."
    "What the hell? She planned this? How long ago?"
    "Whatever, just go with the flow, Anon. You're here to eat some lunch."
    "Lyra shows you to your seat, or pile of hay, as it appears to be."
    "You sit, expecting it to not hold your weight, but your prediction is wrong. Thankfully."
    "In front of you sits what looks like a sandwich and milkshake. Lyra has just a milkshake."
    a "...Well, where's your food?"
    play sound "LyraLine5.mp3"    
    l "Oh, well, I already ate."
    a "Wait... then why did you...?" 
    "You let yourself trail off, unsure whether or not to confront the unicorn in front of you."
    show lyra blush with Dissolve(0.5)
    "You sigh and shake your head, and make eye contact with the now-blushing mare."
    play sound "LyraLine6.mp3"    
    l "Heh. Well, eat up, Anon, it's on me."
    "She laughs sheepishly, a red hue forming on her face while she sips on her milkshake."
    "You roll your eyes and pick up the sandwich and take a bite."
    "...Huh, doesn't really taste like a sandwich. It just tastes like bread and... a leaf?"
    "You open the sandwich and peer into it."
    a "Lyra. You know I don't eat goddamn daffodils."
    "You catch a glance at two ponies who seem to be gossipping about you. One of them giggles."
    "You roll your eyes again."
    show lyra surprised with Dissolve(0.5)
    play sound "LyraLine7.mp3"    
    l "I know, I know. I just thought that maybe the first one you tried wasn't good enough! It's my favourite snack, you know."
    "It seems she's trying to get you more comfortable with the casual cuisine in Equestria, but humans didn't get where they are today by eating daffo-{w}fucking{w}-dils."
    show lyra hoof with Dissolve(0.5)
    "You pick a daffodil out of the sandwich and an idea forms in your mind."
    a "Well. You already ate, but how about you take the daffodils and I take the bread? Seems like a good idea."
    "You really don't want to eat the daffodils or leave any behind. The cooks work hard, after all, you know this from personal experience."
    show lyra blush with Dissolve(0.5)
    "Huh?!"
    "She gasps, entirely not expecting this suggestion, and red cheeks flare up once again."
    play sound "LyraLine8.mp3"    
    l "Oh well, i-if you're considering, then sure..." 
    "She gives you a small smile."
    "So cute!"
    "Without much resistance, a mischievous idea pops into your mind, and you give it absolutely zero risk assessment."
    "Taking a couple of daffodils in your hand, you hold them out to Lyra with a smirk."
    a "Here you go." 
    "You say simply, trying to make it look as casual as possible."
    "Lyra, on the other hand, has a shocked expression on her face, and in a lowered voice whispers to you."
    show lyra surprised with Dissolve(0.5)
    play sound "LyraLine9.mp3"    
    l "Y-You want me to eat that s-straight from your hand?"
    "You tilt your head, almost questioningly."
    a "Of course. Why not?"
    show lyra blush with Dissolve(0.5)
    "She can't refuse now. Glancing left and right, she leans forward and eats a couple of daffodils straight from your hand."
    "So. {w} Fucking. {w} Cute."
    "With the reddest hue you've ever seen on a ponie's face, she eats the rest of the daffodils from your hand."
    "Now that the daffodils gone, all that is left is to consume your bread and milkshake, and get the hell over to Pinkie's place."
    "You giggle to yourself as you raise the bread to your face, in an attempt to hide your amusement at the situation you forced Lyra into."
    "But, she notices, and frowns a bit."
    show lyra mad with Dissolve(0.5)
    play sound "LyraLine10.mp3"    
    l "Anon, you knew that was embarrassing, and yet you still did it."
    "Well, the cat's out of the bag, so you just let yourself have a hearty laugh."
    show lyra hoof with Dissolve(0.5)
    "It was hard keeping that in."
    a "Yeah, you're right. Sorry Lyra. I just can't let an opportunity like that pass me by, it's too damn rich."
    "You wipe a tear from your eye."
    "Was it really that funny?"
    "Yes. Yes it was."
    "She giggles a bit."
    play sound "LyraLine11.mp3"    
    l "Yeah, I guess Pinkie would say the same, too."
    "She's sucking down her shake nervously, as the embarrassment still lingers on her face."
    "You are casually drinking your own, feeling quite pleased with yourself."
    "She finishes first, no doubt trying to remove herself from the situation as fast as possible."
    play sound "LyraLine12.mp3"    
    l "Hey, well, it's been fun, Anon! I'll see you some other time, okay?" 
    "She says it with a nervous smile."
    "You laugh."
    a "Absolutely, Lyra. I hope to see you again soon."
    "You wave your goodbyes and she leaves you to finish your shake."
    "You stand up to leave, dropping a bit on the table as a tip and taking a few moments to stretch before resuming your walk to Pinkie's."
    "You hope Lyra invites you out for lunch again, daffodils sandwich or not."

    stop music fadeout 1.0
    return
