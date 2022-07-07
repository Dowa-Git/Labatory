#define PI 3.14159265359
#define TWO_PI 6.28318530718

float2 iResolution;

float4 Triangle(in float2 uv: TEXCOORD): SV_TARGET
{
    float2 center = 2.0 * float2(uv.xy - 0.5 * iResolution.xy) / iResolution.y;
    int N = 3;

    float a = atan2(uv.x, uv.y) + PI;
    float r = TWO_PI / float(N);
    float d = cos(floor(0.5 + a / r) * r - a) * length(uv);

    return float4(0.41,  0.4, d, 1);
}