import sys

step = sys.argv[1]
N = sys.argv[2]
i = sys.argv[3]
dcache = sys.argv[4]
icache = sys.argv[5]
ep = sys.argv[6]

first_nios2_system = (f"""#include <stdlib.h>
#include <sys/alt_stdio.h>
#include <sys/alt_alarm.h>
#include <sys/times.h>
#include <alt_types.h>
#include <system.h>
#include <stdio.h>
#include <unistd.h>
#include <math.h>

#define step {step}
#define N {N}

#define TYPE float

void generateVector(TYPE x[N])
{{
	int i;
	x[0] = 0;
	for (i = 1; i<N; i++) {{
		x[i] = x[i-1] + step;
	}}
}}

TYPE sumVector (TYPE x[], int M)
{{
	TYPE y = 0.0;
	int i;
	for (i=0; i<M; i++){{
		y += x[i] + x[i]*x[i];
	}}
	return y;
}}

typedef struct{{
	unsigned long ticks;
	TYPE result;
}} RES;

RES run_test(){{
  // Define input vector
  TYPE x[N];

  // Returned result
  TYPE y;

  generateVector(x);

	clock_t exec_t1, exec_t2, ticks;

  exec_t1 = times(NULL);

	y = sumVector(x, N);

  exec_t2 = times(NULL);

  ticks = exec_t2 - exec_t1;

  for(int i = 0; i < 10; i++){{
		y /= 2.0;
	}}

  RES res = {{ticks, y}};

	return res;
}}

typedef struct {{
	int whole;
	int decimal;
}} WholeDecimal;

#define PREC 100000.0
WholeDecimal break_up_float(TYPE v) {{
	int whole = v;
	int decimal = (v-(TYPE)whole)*PREC;

	WholeDecimal res = {{whole, decimal}};

	return res;
}}

#define REPS 10

int main()
{{
	printf("---START {dcache} {icache} {i}---\\n");
	TYPE average_ticks = 0;
	TYPE average_results = 0;
	for(int i = 0; i < REPS; i++){{
		RES results = run_test();
		average_ticks += (TYPE)results.ticks/(TYPE)REPS;
		average_results += (TYPE)results.result/(TYPE)REPS;

//		WholeDecimal average_ticks_i = break_up_float(results.ticks);
//		WholeDecimal average_results_i = break_up_float(results.result);
//		printf("Result: %d.%d took %d.%d ticks\\n", average_results_i.whole, average_results_i.decimal, average_ticks_i.whole, average_ticks_i.decimal);
	}}

  WholeDecimal average_ticks_i = break_up_float(average_ticks);
	WholeDecimal average_results_i = break_up_float(average_results);
  printf("AVG: DCACHE: {dcache} ICACHE: {icache} TEST: {i} STEPS: {N} STEP_SIZE: {step} Result: %d.%d took %d.%d ticks\\n", average_results_i.whole, average_results_i.decimal, average_ticks_i.whole, average_ticks_i.decimal);
  printf("---STOP---\\n");
  return 0;
}}

""");

with open(ep + '/software/hello_world/hello_world.c', 'w') as f:
    f.write(first_nios2_system)
