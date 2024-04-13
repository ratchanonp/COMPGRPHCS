void PrimeRosette(double radius, int n)
{
    int k, j, index;
    polypoint poly;

    buildNgon(radius, n, poly);
    index = 0;
    MoveTo(poly[index]); // start
    for (k = 1; k <= (n - 1) / 2; k++)
        for (j = 0; j < n; j++)
        {
            index = (index + k) mod n + 1;
            drawLineTo(poly[j]);
        }
}
}