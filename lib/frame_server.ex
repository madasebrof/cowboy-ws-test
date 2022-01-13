defmodule FrameServer do
  @behaviour :cowboy_websocket
  require Logger

  def init(req, state) do
    Logger.info("ws - got connection...")
    {:cowboy_websocket, req, state}
  end

  def websocket_handle({_msg_type, _message}, state) do
    # we don't do anything,
    # we just receive the message!
    {:ok, state}
  end

  def websocket_info(_info, state) do
    Logger.warn("ws - websocket_info")
    {:ok, state}
  end

  def terminate(reason, _req, state) do
    Logger.info("ws - disconnected, reason: #{inspect(reason)}, #{inspect(state)}")
    :ok
  end
end
