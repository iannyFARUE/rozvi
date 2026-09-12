from django.shortcuts import render

COVER_GRADIENTS = [
    'from-rose-200 via-orange-100 to-amber-200',
    'from-emerald-200 via-teal-100 to-cyan-200',
    'from-indigo-200 via-violet-100 to-purple-200',
    'from-sky-200 via-blue-100 to-indigo-200',
    'from-amber-200 via-yellow-100 to-lime-200',
    'from-pink-200 via-rose-100 to-red-200',
]

AVATAR_COLORS = [
    'bg-emerald-600',
    'bg-indigo-600',
    'bg-rose-600',
    'bg-amber-600',
    'bg-sky-600',
    'bg-violet-600',
]

_posts_raw = [
    {
        'title': 'Why Django Still Wins for Solo Developers in 2026',
        'excerpt': "Frameworks come and go, but Django's batteries-included "
                   "philosophy keeps paying off when you're shipping alone. "
                   "Here's what keeps me coming back to it for every side project.",
        'author': 'Ian Farai Madhara',
        'topic': 'Software Engineering',
        'date_posted': 'Sep 2, 2026',
        'read_time': 6,
        'claps': 482,
        'comments': 31,
        'featured': True,
    },
    {
        'title': 'A Field Guide to Reading Other People’s Code',
        'excerpt': 'Most of your career will be spent inside codebases you '
                   'did not write. These are the habits that made me faster '
                   'at understanding unfamiliar systems.',
        'author': 'Naomi Chen',
        'topic': 'Career',
        'date_posted': 'Aug 29, 2026',
        'read_time': 8,
        'claps': 915,
        'comments': 64,
        'featured': True,
    },
    {
        'title': 'Postgres Indexes Explained With Pictures',
        'excerpt': 'B-trees, GIN, and BRIN indexes stop being scary once you '
                   'can see how they organize data on disk. A visual walkthrough '
                   'for backend developers.',
        'author': 'Marcus Webb',
        'topic': 'Databases',
        'date_posted': 'Aug 24, 2026',
        'read_time': 11,
        'claps': 1204,
        'comments': 87,
        'featured': True,
    },
    {
        'title': 'I Quit My Job to Write Full-Time. Here’s the Honest Update.',
        'excerpt': 'Six months, no salary, and a lot of self-doubt. A candid '
                   'look at what nobody tells you about leaving stability behind.',
        'author': 'Priya Anand',
        'topic': 'Life',
        'date_posted': 'Aug 20, 2026',
        'read_time': 5,
        'claps': 2310,
        'comments': 142,
        'featured': False,
    },
    {
        'title': 'Designing APIs People Actually Enjoy Using',
        'excerpt': 'Good API design is invisible — it just feels obvious. '
                   'A breakdown of the small decisions that separate a delightful '
                   'SDK from a frustrating one.',
        'author': 'Ian Farai Madhara',
        'topic': 'Software Engineering',
        'date_posted': 'Aug 15, 2026',
        'read_time': 7,
        'claps': 671,
        'comments': 28,
        'featured': False,
    },
    {
        'title': 'The Case for Boring Technology',
        'excerpt': 'Chasing the newest framework has a cost that rarely shows '
                   'up in the demo. Why picking the dull, proven tool is usually '
                   'the ambitious choice.',
        'author': 'Sofia Delgado',
        'topic': 'Opinion',
        'date_posted': 'Aug 9, 2026',
        'read_time': 4,
        'claps': 389,
        'comments': 19,
        'featured': False,
    },
    {
        'title': 'What Building in Public Actually Taught Me',
        'excerpt': 'A year of sharing unfinished work, failed launches, and '
                   'small wins online. The lessons had very little to do with marketing.',
        'author': 'Marcus Webb',
        'topic': 'Startups',
        'date_posted': 'Aug 3, 2026',
        'read_time': 9,
        'claps': 1560,
        'comments': 103,
        'featured': False,
    },
    {
        'title': 'Async Python Without the Headaches',
        'excerpt': 'asyncio has a reputation for being confusing. Once you '
                   'understand the event loop as a single idea, the rest clicks '
                   'into place.',
        'author': 'Naomi Chen',
        'topic': 'Python',
        'date_posted': 'Jul 27, 2026',
        'read_time': 10,
        'claps': 843,
        'comments': 52,
        'featured': False,
    },
]

posts = []
for i, post in enumerate(_posts_raw):
    post = dict(post)
    post['id'] = i + 1
    post['author_initials'] = ''.join(part[0] for part in post['author'].split()[:2]).upper()
    post['avatar_color'] = AVATAR_COLORS[i % len(AVATAR_COLORS)]
    post['cover_gradient'] = COVER_GRADIENTS[i % len(COVER_GRADIENTS)]
    posts.append(post)

staff_picks = [post for post in posts if post['featured']]

topics = [
    'Software Engineering', 'Career', 'Databases', 'Python',
    'Startups', 'Life', 'Opinion', 'Productivity',
]


def home(request):
    context = {
        'posts': posts,
        'staff_picks': staff_picks,
        'topics': topics,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
