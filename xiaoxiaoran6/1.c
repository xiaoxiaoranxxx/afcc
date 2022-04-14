#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define DEPTH 10

typedef int BigInteger[10100];

int comp(const BigInteger a, const int c, const int d, const BigInteger b) //大数比较
{
    int i, t = 0, O = -DEPTH * 2;
    if (b[0] - a[0] < d && c)
        return 1;
    for (i = b[0]; i > d; i--)
    {
        t = t * DEPTH + a[i - d] * c - b[i];
        if (t > 0)
            return 1;
        if (t < O)
            return 0;
    }
    for (i = d; i; i--)
    {
        t = t * DEPTH - b[i];
        if (t > 0)
            return 1;
        if (t < O)
            return 0;
    }
    return t > 0;
}

void sub(BigInteger a, const BigInteger b, const int c, const int d) //大数减
{
    int i, O = b[0] + d;
    for (i = 1 + d; i <= O; i++)
        if ((a[i] -= b[i - d] * c) < 0)
            a[i + 1] += (a[i] - DEPTH + 1) / DEPTH, a[i] -= (a[i] - DEPTH + 1) / DEPTH * DEPTH;
    for (; a[i] < 0; a[i + 1] += (a[i] - DEPTH + 1) / DEPTH, a[i] -= (a[i] - DEPTH + 1) / DEPTH * DEPTH, i++)
        ;
    for (; !a[a[0]] && a[0] > 1; a[0]--)
        ;
}

void Sqrt(BigInteger b, BigInteger a) //开平方
{
    int h, l, m, i;
    memset((void *)b, 0, sizeof(BigInteger));
    for (i = b[0] = (a[0] + 1) >> 1; i; sub(a, b, m, i - 1), b[i] += m, i--)
        for (h = DEPTH - 1, l = 0, b[i] = m = (h + l + 1) >> 1; h > l; b[i] = m = (h + l + 1) >> 1)
            if (comp(b, m, i - 1, a))
                h = m - 1;
            else
                l = m;
    for (; !b[b[0]] && b[0] > 1; b[0]--)
        ;
    for (i = 1; i <= b[0]; b[i++] >>= 1)
        ;
}
// n/166 = 71....
char str[10100] = "710426542430767315216760794114622199691609874204743190419177803336685631663181323322014423739860007487797965472505492560515520347998262609038656216986939090718874499676284246152337203150331278432328271624281993234848078997863629219265115870819791150259792580588801597844476348690113461466450979506426424549999508405668764321788561357788588409902382079078124970997888946423628535870045211475341990922624843345676616546475567376975265965235167219485525557619369272138253902135102109948308463357689863617500147889709178815410667610944325138911775808087960460960848259994197560449857590535712662528798363217559839440";
BigInteger a, b;

int main()
{
    // scanf("%s", str);
    a[0] = strlen(str);
    for (int i = 1; i <= a[0]; i++)
        a[i] = str[a[0] - i] - '0';
    Sqrt(b, a);
    for (int i = b[0]; i >= 1; i--)
        printf("%d", b[i]);
    printf("\n");
    return 0;
}
