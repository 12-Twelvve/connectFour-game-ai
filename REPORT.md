## Complexity of the Problem 

The Connect Four game presents diverse complexities. The game board's 7x6 grid allows token placement in columns, leading to a branching factor in the game tree. Players have multiple column choices, causing the game's complexity to rise exponentially with tree depth.
Our implementation faced the challenge of creating efficient algorithms for move generation, game state evaluation, and decision-making. We employed profiling tools to assess algorithm performance and ensure effectiveness across varying game states.

## AI Techniques Considered

We considered a few AI techniques to make the Connect Four game smart, like basic minimax search and alpha-beta pruning. But we decided on using the minimax algorithm with alpha-beta pruning. This combo is great because it's really good at finding the best move while being mindful of how long it takes.

Minimax is like exploring a map of the game's possible future states. We look ahead a bit and see what might happen. Alpha-beta pruning is a trick that lets us avoid spending too much time on paths that are probably not so good. It's like skipping paths that we're pretty sure won't lead to victory.

This choice is nice because it keeps our AI player strong, while also not taking forever to think. Even though Connect Four has many ways to play, alpha-beta pruning helps us focus on the smartest choices.

## Reflections

While working on the project, we encountered some hurdles. Designing a good way to evaluate the game's current state efficiently was tricky. Also, dealing with the connections between sensors, actuators, and the agent program got a bit complicated. Debugging was tough because everything is linked, and we needed to be sure that they all worked together as expected.Advanced rules in a game can indeed complicate the implementation process and introduce additional challenges. These complexities arise because advanced rules often interact with existing mechanics, requiring careful consideration and integration.

We managed these challenges by taking a step-by-step approach. We tested each part on its own before putting everything together. We used special tests for each component, checking if sensors, actuators, and the agent program worked correctly. Incorporating advanced rules can indeed be challenging, but with careful planning, thorough testing, and a modular design, I was able to successfully implement one of them i.e. popup feature.
