defmodule FrameServer.Application do
  @moduledoc false
  use Application
  require Logger

  @port 8765

  @impl true
  def start(_type, _args) do
    dispatch =
      :cowboy_router.compile([
        {:_,
         [
           {"/", FrameServer, []}
         ]}
      ])

    :cowboy.start_clear(:server, [{:port, @port}], %{:env => %{:dispatch => dispatch}})
  end
end
