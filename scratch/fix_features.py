import re

files = ['fseq.html', 'lazy-serum.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Section wrapper: Make it h-[100svh] on mobile
    content = content.replace(
        'class="features-section py-8 md:pt-4 md:pb-8 bg-black relative flex-none"',
        'class="features-section h-[100svh] md:h-auto flex flex-col justify-center py-4 md:pt-4 md:pb-8 bg-black relative flex-none"'
    )
    
    # Grid gap: reduce to gap-y-3 gap-x-4 on mobile
    content = content.replace(
        'class="grid grid-cols-2 lg:grid-cols-5 gap-6 md:gap-x-8 md:gap-y-6"',
        'class="grid grid-cols-2 lg:grid-cols-5 gap-y-3 gap-x-4 md:gap-x-8 md:gap-y-6"'
    )
    
    # H2 margin: reduce mb-8 to mb-4, text-2xl to text-xl
    content = content.replace(
        'class="text-2xl md:text-3xl font-bold text-white mb-8 md:mb-6 pb-2 md:pb-4 tracking-wider"',
        'class="text-xl md:text-3xl font-bold text-white mb-4 md:mb-6 pb-2 tracking-wider"'
    )
    # Lazy Serum uses uppercase for the header, so replace that too
    content = content.replace(
        'class="text-2xl md:text-3xl font-bold text-white mb-8 md:mb-6 pb-2 md:pb-4 tracking-wider uppercase"',
        'class="text-xl md:text-3xl font-bold text-white mb-4 md:mb-6 pb-2 tracking-wider uppercase"'
    )
    
    # Button margin: reduce mt-12 to mt-6
    content = content.replace(
        'class="mt-12 2xl:hidden flex justify-center"',
        'class="mt-4 md:mt-12 2xl:hidden flex justify-center"'
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
