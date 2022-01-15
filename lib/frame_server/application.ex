defmodule FrameServer.Application do
  @moduledoc false
  use Application
  require Logger

  @port 8765

  # should be at least as big as largest binary message!
  @buf_size 1024 * 1024 * 2

  @impl true
  def start(_type, _args) do
    dispatch =
      :cowboy_router.compile([
        {:_,
         [
           {"/", FrameServer, []}
         ]}
      ])

    :cowboy.start_clear(
      :server,
      # need to increase recbuf, sndbuf, buffer for larger messages!
      [{:recbuf, @buf_size}, {:sndbuf, @buf_size}, {:buffer, @buf_size}, {:port, @port}],
      %{:env => %{:dispatch => dispatch}}
    )
  end
end
