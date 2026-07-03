import re

with open('fseq.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'class="video-page-item h-[100svh] md:h-auto flex flex-col justify-center md:justify-start"',
    'class="video-page-item h-[100svh] md:h-auto flex flex-col justify-center md:justify-start py-16 md:py-0 px-4"'
)

content = content.replace(
    'class="relative aspect-[4/3] rounded-xl overflow-hidden bg-zinc-900 shadow-2xl mb-8 group border border-white/10"',
    'class="relative w-full max-h-[45svh] md:max-h-none shrink min-h-0 aspect-[4/3] rounded-xl overflow-hidden bg-zinc-900 shadow-2xl mb-4 md:mb-8 group border border-white/10"'
)

content = content.replace(
    'class="w-full h-full object-cover" autoplay muted loop playsinline',
    'class="lazy-video w-full h-full object-contain md:object-cover" muted loop playsinline'
)

content = content.replace(
    'class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"',
    'class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"'
)

content = content.replace(
    '<div class="space-y-4">',
    '<div class="space-y-2 md:space-y-4 shrink-0">'
)

content = content.replace(
    'class="text-3xl md:text-5xl font-black text-white tracking-tighter uppercase leading-none"',
    'class="text-2xl md:text-5xl font-black text-white tracking-tighter uppercase leading-none"'
)

content = content.replace(
    'class="text-gray-400 text-lg md:text-xl leading-relaxed max-w-xl"',
    'class="text-gray-400 text-base md:text-xl leading-relaxed max-w-xl"'
)

with open('fseq.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
