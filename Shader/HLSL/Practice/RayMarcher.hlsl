#define MAX_STEPS 100
#define MAX_DIST 100
#define SURF_DIST 0.01

float GetDist(float3 p)
{
    
    return d;
}


float RayMarch(float3 ro, float3 rd)
{
    float d0 = 0.;

    for (int i = 0 ; i < MAX_STEPS; ++i)
    {
        float3 p = ro + rd * d0;

        float ds = length(p);
        d0 += ds;

        if(d0 > MAX_DIST || ds < SURF_DIST)
        {
            break;
        }
    }
    return d0;
}