#!/bin/bash
cat test6_q_50.txt | grep "Still Render" | awk '{sum += $3; n++} END { if (n > 0) print sum / n; }'
