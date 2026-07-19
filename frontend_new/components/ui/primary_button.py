import streamlit as st


def primary_button(
    label: str,
    key: str = None,
    icon: str = "",
    help_text: str = None,
    use_container_width: bool = True,
    disabled: bool = False,
):
    """
    Reusable primary button.

    Parameters
    ----------
    label : str
        Button text

    key : str
        Unique Streamlit key

    icon : str
        Optional emoji icon

    help_text : str
        Tooltip text

    use_container_width : bool
        Expand to full width

    disabled : bool
        Disable button
    """

    button_label = f"{icon} {label}" if icon else label

    return st.button(
        label=button_label,
        key=key,
        help=help_text,
        type="primary",
        use_container_width=use_container_width,
        disabled=disabled,
    )
