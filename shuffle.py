import re
import random

with open('/Users/nikhi/WeddingWeb/gallery.html', 'r') as f:
    content = f.read()

# Extract the gallery grid block
grid_match = re.search(r'(<div class="gallery-grid">)(.*?)(    </div>\n  </section>)', content, re.DOTALL)
if not grid_match:
    print("Could not find gallery grid")
    exit(1)

prefix = content[:grid_match.start(2)]
grid_content = grid_match.group(2)
suffix = content[grid_match.end(2):]

cells = re.findall(r'(\s*<div class="gallery-cell">.*?</div>)', grid_content, re.DOTALL)

# Classify
groups = []
couples = []

group_kws = ['friends', 'family', 'group', 'together', 'cowboy', 'loved ones', 'gathering', 'dining']

for c in cells:
    alt = re.search(r'alt="(.*?)"', c).group(1).lower()
    is_group = any(kw in alt for kw in group_kws) and 'lovely moment together' not in alt and 'walking together' not in alt
    if is_group:
        groups.append(c)
    else:
        couples.append(c)

print(f"Couples: {len(couples)}, Groups: {len(groups)}")

# Shuffle to mix green saree (contiguous numbers)
random.seed(12345)
random.shuffle(couples)
random.shuffle(groups)

# Interleave
result_cells = []
num_couples = len(couples)
num_groups = len(groups)

if num_groups == 0:
    result_cells = couples
else:
    # We create (num_groups) bins of couples
    bins = [[] for _ in range(num_groups)]
    for i, c in enumerate(couples):
        bins[i % num_groups].append(c)
        
    for i in range(num_groups):
        result_cells.extend(bins[i])
        result_cells.append(groups[i])

new_grid_content = "\n" + "".join(result_cells) + "\n"

new_content = prefix + new_grid_content + suffix

with open('/Users/nikhi/WeddingWeb/gallery.html', 'w') as f:
    f.write(new_content)

print("Done shuffling.")
