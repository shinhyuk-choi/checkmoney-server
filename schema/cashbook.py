from drf_spectacular.utils import extend_schema, OpenApiParameter


class CashBookSchema:
    list_schema = dict(
        name="chltlsgur",
        decorator=extend_schema(
            parameters=[
                OpenApiParameter(
                    name="Authorization",
                    type=dict,
                    location=OpenApiParameter.HEADER,
                    required=True,
                    description="Token {token_key}"
                )

            ]
        )
    )
